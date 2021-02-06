song_albums = [
    ("Lost sky", "fearlerss"),
    ("Wishing well", "Juice wrld"),
    ("Avicii", "Silhoutets"),
    ("Python", "Programming"),
]

for artist, song in song_albums:
    print("Artist is {}, and song would be {}"
          .format(artist, song))
    if artist == "Python":
        print(artist, song)
