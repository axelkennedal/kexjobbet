import numpy as np
from random import shuffle
from sklearn.svm import SVC
from mutagen.id3 import ID3
import warnings

## Generates a pair list from a dictionary containing
## the various mfccs and genre hashes. Allows us to shuffle the
## list without loosing the song mfcc/genre relation.
##
## Input:
##      data - {'data': [mfccs], 'group': groups} (output from 
##              generate_feature_vector)
##      
## Output:
##      pairList - A list of each mfcc/genre association [(mfccs, genre)]
def generate_pair_list(data):
    res = []

    for index in range(0, len(data['data'])):
        res.append((data['data'][index], data['group'][index]))

    return res
        
## Generates a balanced training, classify set from a pairList
##
## Input:
##      pairList - list of pairs
##      split - Data split percentage (0, 1)
##
## Output:
##      [training, classify] training, classify - pairList
def generate_training_classify_set(pairList, split = 0.7):
    genres = {}
    training = []
    classify = []

    if split <= 0 or 1 <= split:
        warnings.warn('Invalid split index')
        splitIndex = 0.7

    ## Order by genre
    for (data, genre) in pairList:
        if genre not in genres.keys():
            genres.update({ genre: [(data, genre)] })
        else:
            genres[genre].append((data, genre))

    for genreHash in genres:
        splitIndex = int(len(genres[genreHash])*split)
        training += genres[genreHash][:splitIndex]
        classify += genres[genreHash][splitIndex:]
    
    return (training, classify)

## Train and classifies the SVM with nIter different permutations
## of the data (pairList).
##
## Input:
##      pairList - mfcc data [(mfcc, genreHash)]
##      nIter - number of iterations to run
##
## Output:
##      A list containing the success rate for each run.
def run_repeated_tests(pairList, nIter):
    iterationResults = []
    first = lambda y: map(lambda x: x[0], y)
    second = lambda y: map(lambda x: x[1], y)


    for i in range(0, nIter):
        svc = SVC(gamma = 3, tol = 0.00005)

        shuffle(pairList)
        (training, classify) = generate_training_classify_set(pairList)
        svc.fit(list(first(training)), list(second(training)))

        classRes = svc.predict(list(first(classify)))
        expected = list(second(classify))

        hits = 0
        for j in range(0, len(classRes)):
            if classRes[j] == expected[j]:
                hits += 1

        iterationResults.append(hits / len(classRes))
        
    return iterationResults
        

