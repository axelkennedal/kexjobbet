import os
import sys
from collections import Counter
from mp3_tagger import MP3File, VERSION_2
from mutagen.mp3 import MP3

relative_folder_path = "./sample_music"

def fix_genres(genres_to_fix):
    print("Searching for songs with genre " + str(genres_to_fix) + "...\n")

    fixed_songs = []
    for file in os.listdir(relative_folder_path):
        if file.endswith(".mp3"):
            mp3 = MP3File(os.path.join(relative_folder_path, file))
            mp3.set_version(VERSION_2)
            old_genre = str(mp3.genre)
            print(old_genre, end=", ")
            sys.stdout.flush()
            if old_genre in genres_to_fix:
                print("\nFound match: " + file)
                print("For genre to fix: " + old_genre)
                new_genre = input("Enter new Genre: ")
                mp3.genre = new_genre
                mp3.save()
                fixed_songs += (mp3, old_genre)

    print("\n\nFixed " + str(len(fixed_songs)) + " songs")
    #print("---Summary---")

    #for fixed_song, old_genre in fixed_songs:
    #    print(str(fixed_song.song) + " " + old_genre + " -> " + str(fixed_song.genre))

def fix_specific(filepath):
    print("Fixing genre for specific song...")
    mp3 = MP3File(filepath.replace("\\", ""))
    mp3.set_version(VERSION_2)
    old_genre = str(mp3.genre)
    print("Genre to fix: " + old_genre)
    new_genre = input("Enter new genre: ")
    mp3.genre = new_genre
    mp3.save()
    print("Fixed!")

def fix_missing():
    for file in os.listdir(relative_folder_path):
        print(".", end="")
        sys.stdout.flush()

        if file.endswith(".mp3"):
            mp3 = MP3File(os.path.join(relative_folder_path, file))
            mp3.set_version(VERSION_2)

            old_genre = str(mp3.genre)
            old_artist = str(mp3.artist)
            old_title = str(mp3.song)

            if is_missing(old_genre) :
                print("\nMissing genre for " + file)
                mp3.genre = input("Enter new genre: ")
            if is_missing(old_artist):
                print("\nMissing artist for " + file)
                mp3.artist = input("Enter new artist: ")
            if is_missing(old_title):
                print("\nMissing title for " + file)
                mp3.song = input("Enter new title: ")
            mp3.save()

def clean_tags():
    for file in os.listdir(relative_folder_path):
        print(".", end="")
        sys.stdout.flush()

        if file.endswith(".mp3"):
            mp3 = MP3File(os.path.join(relative_folder_path, file))
            mp3.set_version(VERSION_2)

            mp3.genre = clean_tag(mp3.genre)
            mp3.artist = clean_tag(mp3.artist)
            mp3.song = clean_tag(mp3.song)
            del mp3.comment
            del mp3.copyright
            del mp3.url
            del mp3.band
            del mp3.composer
            mp3.save()

def list_low_quality():
    quality_songs = []
    for file in os.listdir(relative_folder_path):
        print(".", end="")
        sys.stdout.flush()
        if file.endswith(".mp3"):
            try:
                mp3 = MP3(os.path.join(relative_folder_path, file))
                bitrate = mp3.info.bitrate / 1000
                quality_songs.append(str(bitrate))
                if bitrate < 315:
                    print("\n" + str(bitrate) + "kbps: " + file)
            except:
                print("error reading " + file)

    print("")
    quality_distribution = Counter(quality_songs).most_common()

    csv_file = open("quality_distribution.csv", "w")
    csv_file.write("Quality,Percentage,Number of Songs\n")
    for quality, count in quality_distribution:
        percentage = str(round(count/824 * 100, 2))
        print(percentage + "%\t" + quality + " (" + str(count) + " songs)")
        csv_file.write(quality + "," + percentage + "," + str(count) + "\n")

    csv_file.close()

def is_missing(string):
    return string == "" or string == "[]" or string == "None"

def clean_tag(tag):
    if is_missing(tag): return ""
    return str(tag).replace("[", "(").replace("]", ")").strip()

mode = sys.argv[1]
if mode == "genres":
    fix_genres(sys.argv[2:])
elif mode == "specific":
    fix_specific(sys.argv[2])
elif mode == "missing":
    fix_missing()
elif mode == "clean":
    clean_tags()
elif mode == "quality":
    list_low_quality()

print("")
