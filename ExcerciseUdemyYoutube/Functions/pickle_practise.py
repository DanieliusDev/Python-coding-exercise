import pickle

movies = (
    'action',
    'The Rock',
    2010,
    (
        (1, "Jumanji"),
        (2, "Fast 5"),
        (3, "Shazam"),
        (4, "fast 10")))

# with open("movies.pickle", 'wb') as movie_file:
#     pickle.dump(movies, movie_file)


with open("movies.pickle", 'rb') as movie_filed:
    movie2 = pickle.load(movie_filed)

print(movie2)

genre, actor, year_make, movie_list = movie2
print(genre)
print(actor)
print(year_make)

for movie in movie_list:
    movie_number, movie_name = movie
    print(movie_name, movie_number)
