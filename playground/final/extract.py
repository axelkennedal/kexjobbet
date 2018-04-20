from enum import Enum, unique
import mutagen
from mutagen.mp3 import MP3
import librosa
import numpy as np
from multiprocessing import Pool, Value
import random

duration = 30
offset = 0
nMfcc = 20
sampleRate = 44100

counter = None
offsetMode = None

## Extract the genre from the metadata of the specified file.
## Input:
##        filename - name of the file to extract the data from.
## Output:
##        string - file genre
def get_genre(filename):
    genre = mutagen.File(filename)['TCON'].text[0]

    ## Changes Live Electronics to Electronic
    genre = 'Electronic' if genre == 'Live Electronics' else genre

    return genre

## Extract the song length from the metadata of the specified file.
## Input:
##      filename - name of the file to extract the data from.
## Output:
##      float - song length in seconds
def get_length(filename):
    audio = MP3(filename)
    return int(audio.info.length)

## An enum for choosing what kind of offset to use for feature extraction
@unique
class OffsetMode(Enum):
    START = 1
    MIDDLE = 2
    END = 3
    RANDOM = 4

def get_offset_for_mode(filename, mode):
    if mode == OffsetMode.START:
        return 0
    elif mode == OffsetMode.MIDDLE:
        return int((get_length(filename) / 2) - (duration / 2))
    elif mode == OffsetMode.END:
        offset = int(get_length(filename) - duration - 1)
        if offset < 0:
            offset = 0

        return offset
    elif mode == OffsetMode.RANDOM:
        return random.uniform(0, get_length(filename) - duration)
    else:
        print("Unsupported OffsetMode")
        sys.exit(1)

## Extract the feature vectors from the specified file. The mean
## of each coefficient is used as a representation.
## Input:
##      filename - name of the file to extract the features from
## Output:
##      np.array(featureVector) - based on mfcc (normalized)
def get_feature_vector(filename):
    featureVector = []
    fileData, sr = librosa.load(filename, sr = sampleRate, duration = duration, offset = get_offset_for_mode(filename, offsetMode))

    ## We don't want to extract features from songs that are too short
    ## this mess up the dimensions of the resulting feature matrix
    if (len(fileData) != sr * duration):
        return None

    mfccs = librosa.feature.mfcc(fileData, sampleRate, n_mfcc = nMfcc)

    for freq in range(0, len(mfccs[0])):
        featureVector.append(np.mean([mfccs[k][freq] for k in range(0, nMfcc)]))

    return list(np.array(featureVector) / np.linalg.norm(featureVector))

## Extract the features and genre from the specified files.
## Input:
##      filenames - list of filenames to process
##
## Output: { 'data': [], 'group': [] }
##      Dictionary containing the features associated with each file
##      and the associated class.
##
def extract_feature_and_class(filenames):
    songHashGenreName = {}
    trainingData = { 'data': [], 'group': [] }

    for filename in filenames:
        fileGenre = get_genre(filename)
        featureVector = get_feature_vector(filename)

        if (featureVector == None):
            continue

        ## Discard data where the dimension of the feature vector does not match the dimension
        ## of the other feature vectors. This should never happen since supposing that the
        ## sample rate of the data, and the number of samples available matches.
        if (trainingData['data'] != []):
            if(len(trainingData['data'][-1]) != len(featureVector)):
                continue

        genreHash = hash(fileGenre)
        if (genreHash not in songHashGenreName):
            songHashGenreName.update({genreHash: fileGenre})

        trainingData['data'].append(featureVector)
        trainingData['group'].append(genreHash)

        with counter.get_lock():
            counter.value += 1

    return (trainingData, songHashGenreName)

## Split data and create processes.
## Input:
##      filenames - names of files to process
##      jobs - Number of jobs to run in parallel
##
## Output:
##      ({data, groups}, songHashDict)
def generate_feature_vector(filenames, jobs, offsetModeParam, durationParam):
    global counter
    counter = Value('i', 0)

    global offsetMode
    offsetMode = offsetModeParam

    global duration
    duration = durationParam

    if jobs > len(filenames):
        jobs = len(filenames)

    args = []
    chunkSize = int(len(filenames) / jobs)
    for i in range(1, jobs):
        args.append(filenames[(i-1)*chunkSize:i*chunkSize])

    args.append(filenames[(jobs-1)*chunkSize:])

    with Pool(processes = jobs) as pool:
        data = pool.map_async(extract_feature_and_class, args)

        while not data.ready():
            print_progress(counter.value, len(filenames), "")
            data.wait(1)

        data = data.get()
        pool.close()

        print_progress(counter.value, len(filenames), "\n\r")

        resData = { 'data': [], 'group': [] }
        resGenre = { }
        for (d, genreHash) in data:
            resGenre.update(genreHash)
            resData['data'] +=d['data']
            resData['group'] += d['group']

        return (resData, resGenre)

## Prints a progress bar
## Input:
##      cur - current file
##      tot - total number of files
##      end - end string
def print_progress(cur, tot, end):
    nHash = 50
    step = tot / nHash

    pgText = "\rProgress: ["
    for i in range(1, nHash + 1):
        if cur >= int(step*i):
            pgText += "#"
        else:
            pgText += " "

    pgText += "] ({}/{})"
    print(pgText.format(cur, tot), end=end)
