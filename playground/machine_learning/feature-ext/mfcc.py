import librosa
import librosa.display
import matplotlib.pyplot as plt

# Audio file path
audioFile = librosa.util.example_audio_file()

# y: audio time series
# sr: sampling rate of y
y, sr = librosa.load(audioFile)

# Returns mfcc sequence
mfccSeq = librosa.feature.mfcc(y, sr, n_mfcc = 20)

plt.subplot()
librosa.display.specshow(mfccSeq, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()
