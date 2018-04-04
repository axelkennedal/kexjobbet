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

    return trainingData, songHashGenreName
