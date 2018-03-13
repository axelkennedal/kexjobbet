genres_count = {}
genres = ["house", "pop", "house"]

# first add the keys
for genre in genres:
    genres_count[genre] = 0

# then count
for genre in genres:
    genres_count[genre] += 1

print(genres_count)
