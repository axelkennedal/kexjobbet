import os
from shutil import copyfile

NNMD_path = "/home/nicklas/KTH/kexdata/shared/newSet/"
output_path = NNMD_path + "NNMD_out/"
output_test_folder_name = "classify"
output_training_folder_name = "training"

# specify how many files to get from each genre

def generate_training_test_split(songs_per_genre=50, test_split=0.3):
    print("Selecting files...")
    selected_files = {}
    for name in [name for name in os.listdir(NNMD_path) if not name.startswith('.')]:
        genre_folder_path = os.path.join(NNMD_path, name)
        if os.path.isdir(genre_folder_path):
            all_songs_for_genre = [song_name for song_name in os.listdir(genre_folder_path) if song_name.endswith(".mp3")]
            if not name in selected_files:
                selected_files.update({name: []})
            for song in all_songs_for_genre[:songs_per_genre]:
                selected_files[name].append(str(os.path.join(genre_folder_path, song)))

    # Create a test/training split
    print("Creating test/training split...")
    test_files = []
    training_files = []
    for genre in selected_files:
        split_index = int(round(len(selected_files[genre]) * test_split))
        test_files.extend(selected_files[genre][:split_index])
        training_files.extend(selected_files[genre][split_index:])

    # Copy the selected files to the destination
    print("Copying selected files to " + output_path)
    output_test_path = os.path.join(output_path, output_test_folder_name)
    output_training_path = os.path.join(output_path, output_training_folder_name)

    if not os.path.exists(output_test_path):
        os.makedirs(output_test_path)

    if not os.path.exists(output_training_path):
        os.makedirs(output_training_path)

    print("Copying test files...")
    file_no = 1
    for filepath in test_files:
        destination = os.path.join(output_test_path, str(file_no) + ".mp3")
        copyfile(filepath, destination)
        print(str(file_no) + "/" + str(len(test_files)))
        file_no += 1

    print("Copying training files...")
    file_no = 1
    for filepath in training_files:
        copyfile(filepath, os.path.join(output_training_path, str(file_no) + ".mp3"))
        print(str(file_no) + "/" + str(len(training_files)))
        file_no += 1

    print("Finished generating testing and training data")

generate_training_test_split()
