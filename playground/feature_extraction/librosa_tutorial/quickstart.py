from __future__ import print_function
import librosa

# Get file path to included example
filename = librosa.util.example_audio_file()
print(filename)

# Load audio as waveform "y", store sampling rate as "sr"
# IMPORTANT: By default the audio is mixed to mono and
# resampled to 22050 Hz
y, sr = librosa.load(filename)

# Run default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print("Estimated tempo: {:.2f} beats per minute".format(tempo))

# Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print("Saving output to beat_times.csv")
librosa.output.times_csv("beat_times.csv", beat_times)
