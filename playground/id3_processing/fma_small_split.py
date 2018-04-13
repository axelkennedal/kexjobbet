####################################################
# Creates a training/test split from an FMA dataset.
####################################################

import os
import mutagen
from collections import Counter
from shutil import copyfile

fma_small_path          = "../../data/fma_small/"
training_output_folder  = "../../data/fma_output/training/"
testing_output_folder   = "../../data/fma_output/testing/"
test_split = 0.3

# Create a dictionary mapping of genres to filenames
genres = {}
for dirpath, dirnames, files in os.walk(fma_small_path):
    for name in files:
        if name.endswith(".mp3"):
            full_path = os.path.abspath(os.path.join(dirpath, name))
            mutagen_file = mutagen.File(full_path)
            genre = ""
            if "TCON" in mutagen_file:
                genre = mutagen_file["TCON"].text[0]
            if not genre in genres:
                genres.update({genre: []})
            genres[genre].append(str(full_path))

genres_count = {}
for genre in genres:
    genres_count[genre] = len(genres[genre])

sorted_genres = Counter(genres_count).most_common();
for genre, count in sorted_genres:
    print(genre, count)

# Select a subset of all files
selected_genres = ["Hip-Hop", "Electronic", "Pop", "Rock", "Jazz"]
smallest_genre = genres_count[selected_genres[0]]
for genre in selected_genres:
    if genres_count[genre] < smallest_genre:
        smallest_genre = genres_count[genre]

genres_subset = {}
for genre in selected_genres:
    genres_subset[genre] = genres[genre][:smallest_genre]

# Create a test/training split
test_files = []
training_files = []
for genre in genres_subset:
    print(genre)
    split_index = int(round(len(genres_subset[genre]) * test_split))
    print(split_index)
    test_files.extend(genres_subset[genre][:split_index])
    training_files.extend(genres_subset[genre][split_index:])

# Copy the selected files to the destination
if not os.path.exists(testing_output_folder):
    os.makedirs(testing_output_folder)

if not os.path.exists(training_output_folder):
    os.makedirs(training_output_folder)

file_no = 0
for filepath in test_files:
    destination = os.path.join(testing_output_folder, str(file_no) + ".mp3")
    print(destination)
    copyfile(filepath, destination)
    file_no += 1

file_no = 0
for filepath in training_files:
    copyfile(filepath, os.path.join(training_output_folder, str(file_no) + ".mp3"))
    file_no += 1
