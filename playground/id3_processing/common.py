import mutagen

def get_genre(filepath):
    mutagen_file = mutagen.File(filepath)
    genre = ""
    if "TCON" in mutagen_file:
        genre = mutagen_file["TCON"].text[0]
    return genre
