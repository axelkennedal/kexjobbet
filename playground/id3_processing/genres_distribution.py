import os
import sys
import time
from collections import Counter
from mp3_tagger import MP3File, VERSION_2

start_time = time.time()
genres = []

# count the number of songs
number_of_songs = 0
for file in os.listdir("./sample_music"):
    if file.endswith(".mp3"):
        number_of_songs += 1

print("Processing " + str(number_of_songs) + " songs...")

# get all of the genres
current_song = 1
for file in os.listdir("./sample_music"):
    if file.endswith(".mp3"):
        mp3 = MP3File(os.path.join("./sample_music", file))
        mp3.set_version(VERSION_2)
        genres.append(str(mp3.genre))
        print(str(current_song) + " / " + str(number_of_songs) + " = " + str(format(100 * current_song/number_of_songs, ".1f") + "%"),
        end="\r")
        current_song += 1
print("-----------------------------------------------------------------------------------------------")

# compile genres
print("Compiling data...")
genres_count = Counter(genres).most_common()

# print results
csv_file = open("genres_distribution.csv", "w")
csv_file.write("Genre,Percentage,Number of Songs\n")
for genre, count in genres_count:
    percentage = str(round(count/number_of_songs * 100, 2))
    print(percentage + "%\t" + genre + " (" + str(count) + " songs)")
    csv_file.write(genre + "," + percentage + "," + str(count) + "\n")

csv_file.close()

print("--Completed in " + str(round(time.time() - start_time, 2)) + " seconds--")
