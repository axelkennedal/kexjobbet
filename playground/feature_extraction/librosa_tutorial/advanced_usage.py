import numpy as np
import librosa

y, sr = librosa.load(librosa.util.example_audio_file())

# set hop length; at 22050Hz 512 samples ~= 23ms
hop_length = 512

# separate harmonics and percussives into two waveforms
y_harmonic, y_percussive = librosa.effects.hpss(y)

#librosa.output.write_wav("./harmonic.wav", y_harmonic, sr)
#librosa.output.write_wav("./percussive.wav", y_percussive, sr)

# Beat track on the percussive signal
tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)

# compute MFCC features from the raw signal
mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=20)

# and the first order differences (delta features)
mfcc_delta = librosa.feature.delta(mfcc)

# stack and synchronize between beat events
# this time, we'll use the mean value (default) instead of median
beat_mfcc_delta = librosa.util.sync(np.vstack([mfcc, mfcc_delta]), beat_frames)

# compute chroma features from the harmonic signal
chromagram = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)

# aggregate chroma features between beat events
# we'll use the mediam value of each feature between beat frames
beat_chroma = librosa.util.sync(chromagram, beat_frames, aggregate=np.median)

# finally, stack all beat_synchronous features together
beat_features = np.vstack([beat_chroma, beat_mfcc_delta])
