import librosa
import numpy as np
import random
import sklearn.svm as svm
import warnings

filedata, sr = librosa.load(librosa.util.example_audio_file())

allData = []
groups = []

for i in range(int(50 / 10)):
    groups.append(1)
    groups.append(-1)

random.shuffle(groups)

for region in range(int(50 / 5)):
    tmpData = filedata[region * sr * 5: (region + 1) * sr * 5]

    tmpList = []
    mfccs = librosa.feature.mfcc(tmpData, sr=sr, n_mfcc=20)
    for mfcc in mfccs:
        tmpList += mfcc.tolist()
        
    allData.append(tmpList)


clf = svm.SVC()
clf.fit(np.array(allData), np.array(groups))

data = filedata[11 * sr * 5: 12 * sr * 5]
mfccs = librosa.feature.mfcc(data, sr=sr, n_mfcc=20)

list = []
for mfcc in mfccs:
    list += mfcc.tolist()


print(clf.predict(np.array(list).reshape(1, -1)))
