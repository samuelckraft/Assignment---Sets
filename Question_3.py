#Task 1

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set(artist_names)

if len(artist_names) > len(unique_artists):
    print("Duplicate playlists found: True")