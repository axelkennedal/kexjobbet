from extract import *
import glob
import sklearn.svm as svm
import numpy as np
from sklearn.preprocessing import normalize

dataBaseDir = '../../../data/'

trainingData = { 'data': [], 'group': [] }
songHashGenreName = {}

print('Extracting features...')
## Generate sample, feature vector matrix (training data)
filenames = glob.glob(dataBaseDir + 'training/*.mp3')

trainingData, songHashGenreName = extract_feature_and_class(filenames)
data = np.array(trainingData['data'])
group = np.array(trainingData['group'])

data.tofile('mfccdata.dat')
group.tofile('gdata.dat')
# data = np.fromfile('mfccdata.dat', dtype = float).reshape(125,12)
# group = np.fromfile('gdata.dat', dtype = int)


print('\nTraining classifier...')
# Generate classifier model
classifier = svm.SVC(kernel = 'rbf', gamma = 1/10, C = 100, tol = 0.00001)
classifier.fit(data, group)
print('Score: %f' % classifier.score(data, group))

# Attempt to predict data
total = 0
hit = 0
for filename in glob.glob(dataBaseDir + 'classify/*.mp3'):
    expected = hash(get_genre(filename))
    result = classifier.predict(np.array(get_feature_vector(filename)).reshape(1, -1))

    if (expected == result[0]):
        hit += 1
    else:
        print ("Classified %s as %s\n\tSong: %s" % (songHashGenreName[expected], songHashGenreName[list(result)[0]], filename))

    total += 1

print("\n\nFinished classifying %d songs." % total)
print("Accuracy {}% [{}/{}]".format(100 * hit / total, hit, total))
