from extract import *
import glob
import sklearn.svm as svm
import numpy as np

dataBaseDir = '../../../data/'

trainingData = { 'data': [], 'group': [] }
songHashGenreName = {}

def main():
    print('Extracting features...')
    ## Generate sample, feature vector matrix (training data)
    filenames = glob.glob(dataBaseDir + 'training/*.mp3')

    trainingData, songHashGenreName = extract_feature_and_class(filenames)
    data = np.array(trainingData['data'])
    group = np.array(trainingData['group'])

    # np.savetxt('mfccdata.dat', data)
    # np.savetxt('gdata.dat', group)
    # data = np.loadtxt('mfccdata.dat', dtype=float)
    # group = np.loadtxt('gdata.dat', dtype=float)

    print('\nTraining classifier...')
    # Generate classifier model
    classifier = svm.SVC(kernel = 'rbf', gamma = 1, C = 50, tol = 0.00001)
    classifier.fit(data, group)
    print('Score: %f' % classifier.score(data, group))

    # Get predict data
    print('Classifying data.')
    filenames = glob.glob(dataBaseDir + 'classify/*.mp3')
    predictDataDict, _ = extract_feature_and_class(filenames)
    predictGenre = np.array(predictDataDict['group'])
    predictData = np.array(predictDataDict['data'])

    # np.savetxt('predData.dat', predictData)
    # np.savetxt('predGroup.dat', predictGenre)
    # predictData = np.loadtxt('predData.dat', dtype=float)
    # predictGenre = np.loadtxt('predGroup.dat', dtype=float)

    result = classifier.predict(predictData)

    hit = 0
    for i in range(0, len(result)):
        if result[i] == predictGenre[i]:
            hit += 1

    print("\n\nFinished classifying %d songs." % len(result))
    print("Accuracy {}% [{}/{}]".format(100 * hit / len(result), hit, len(result)))

if __name__  == '__main__':
    main()