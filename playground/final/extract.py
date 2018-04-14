import mutagen
import librosa
import numpy as np
from multiprocessing import Pool

duration = 30
offset = 0
nMfcc = 20
sampleRate = 44100

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

## Extract the feature vectors from the specified file. The mean 
## of each coefficient is used as a representation. 
## Input:
##      filename - name of the file to extract the features from
## Output:
##      np.array(featureVector) - based on mfcc (normalized)
def get_feature_vector(filename):
    featureVector = []
    fileData, sr = librosa.load(filename, sr = sampleRate, duration = duration, offset = offset)

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
    nFile = 1

    for filename in filenames:
        print("Processing file {} of {}...".format(nFile, len(filenames)))
        nFile += 1
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

    return (trainingData, songHashGenreName)

## Split data and create processes.
## Input:
##      filenames - names of files to process
##      jobs - Number of jobs to run in parallel
##
## Output:
##      ({data, groups}, songHashDict)
def generate_feature_vector(filenames, jobs):
    if jobs > len(filenames):
        jobs = len(filenames)

    args = []
    chunkSize = int(len(filenames) / jobs)
    for i in range(1, jobs):
        args.append(filenames[(i-1)*chunkSize:i*chunkSize])

    args.append(filenames[(jobs-1)*chunkSize:])

    if len(filenames) == 90:
        with open('dump', 'w') as f:
            for s in args:
                for v in s:
                    f.write(v)

    with Pool(processes = jobs) as pool:
        data = pool.map(extract_feature_and_class, args)

        resData = { 'data': [], 'group': [] }
        resGenre = { }
        for (d, genreHash) in data:
            resGenre.update(genreHash)
            resData['data'] +=d['data']
            resData['group'] += d['group']

        return (resData, resGenre)
