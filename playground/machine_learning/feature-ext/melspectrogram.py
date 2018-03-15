import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as ms

ms.use('seaborn-muted')

import IPython.display
import librosa
import librosa.display

audioPath = librosa.util.example_audio_file()

y, sr = librosa.load(audioPath)

# Create a mel-scaled power spectrogram
S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)

# Convert to log sacale (dB) using peak max power as reference.
logS = librosa.power_to_db(S, ref=np.max)

# New figure
plt.figure(figsize=(12, 4))

# Display spectrogram
librosa.display.specshow(logS, sr=sr, x_axis='time', y_axis='mel')

plt.title('mel power spectrogram')
plt.colorbar(format='%+02.0f db')
plt.tight_layout()
plt.show()
          

