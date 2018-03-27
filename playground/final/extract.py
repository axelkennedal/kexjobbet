import mutagen
import librosa

duration = 30
offset = 20
nMfcc = 12
sampleRate = 44100

## Extract the genre from the metadata of the specified file.
## Input:
##		filename - name of the file to extract the data from.
## Output:
##		string - file genre 
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

	mfccs = librosa.feature.mfcc(fileData, sampleRate, n_mfcc = nMfcc) 
	for mfcc in mfccs:
		tmplist = list(mfcc)
		featureVector.append(sum(tmplist) / len(tmplist))

	return featureVector
