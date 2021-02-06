movies = [("Rocky", "Silvester Stallone", 1990),
          ("Terminator", "Arnold Schwartz", 1998),
          ("Blade", "Wesley Snipes", 2000)
          ]

print(len(movies))

for movie_name, actor_name, year in movies:
    print("Movie: {}, whos actor is {}, which was made in {}"
          .format(movie_name, actor_name, year))
