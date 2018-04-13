#########################################################
# Organizes audio files into folders based on their genre
#########################################################

import os
from shutil import copyfile
from common import get_genre

selected_genres = ["Hip-Hop", "Electronic", "Pop", "Rock", "Jazz"]
input_path = "../../data/fma_small/"
output_path = "../../data/genres/"

print("Filtering songs for selected genres...")
selected_files = {}
for dirpath, dirnames, files in os.walk(input_path):
    for name in files:
        if name.endswith(".mp3"):
            full_path = os.path.abspath(os.path.join(dirpath, name))
            genre = get_genre(full_path)
            if genre in selected_genres:
                if not genre in selected_files:
                    selected_files.update({genre: []})
                selected_files[genre].append(str(full_path))

print("Creating genre folders and copying files...")

for genre in selected_files:
    genre_output_folder = output_path + genre + "/"
    if not os.path.exists(genre_output_folder):
        os.makedirs(genre_output_folder)
    file_no = 0
    for sourcepath in selected_files[genre]:
        destination = genre_output_folder + str(file_no) + ".mp3"
        print(destination)
        copyfile(sourcepath, destination)
        file_no += 1
