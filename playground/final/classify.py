from extract import *
import glob
import sklearn.svm as svm
import numpy as np
from sklearn.preprocessing import normalize

dataBaseDir = '../../../kexdata/'

trainingData = { 'data': [], 'group': [] }
songHashGenreName = {}

## Generate sample, feature vector matrix (training data)
for filename in glob.glob(dataBaseDir + 'training/*.mp3'):
	featureVector = get_feature_vector(filename)
	fileGenre = get_genre(filename)

	## Discard data where the dimension of the feature vector does not match the dimension
	## of the other feature vectors.
	if (trainingData['data'] != []):
		if(len(trainingData['data'][-1]) != len(featureVector)):
			continue

	genreHash = hash(fileGenre)
	if (genreHash not in songHashGenreName):
		songHashGenreName.update({genreHash: fileGenre})

	trainingData['data'].append(featureVector)
	trainingData['group'].append(genreHash)

# Generate classifier model
classifier = svm.SVC(kernel = 'rbf', gamma = 'auto', C = 1)
classifier.fit(normalize(np.array(trainingData['data']), axis=0), np.array(trainingData['group']))
print(classifier.score(normalize(np.array(trainingData['data']), axis=0), np.array(trainingData['group'])))

# Attempt to predict data
total = 0;
hit = 0;
for filename in glob.glob(dataBaseDir + 'classify/*.mp3'):
	expected = hash(get_genre(filename))
	result = classifier.predict(np.array(get_feature_vector(filename)).reshape(1, -1))

	if (expected == result):
		hit += 1
	else:
		print ("Classified %s as %s\n\tSong: %s" % (songHashGenreName[expected], songHashGenreName[list(result)[0]], filename))

	total += 1

print("\n\nFinished classifying %d songs." % total)
print("Accuracy {}% [{}/{}]".format(100 * hit / total, hit, total))
