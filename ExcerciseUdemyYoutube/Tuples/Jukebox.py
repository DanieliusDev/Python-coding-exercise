from nested_data import albums

user_input = input("Welcome to Jukebox, Hit enter to START")

while True:
    for index, (title, artist, year, songs) in enumerate(albums):
        print(index + 1, title)
    user_input = int(input())
    if 1 <= user_input <= len(albums):
        for numb, name in songs:
            print(numb, name)
        user_input = int(input())
        if 1 <= user_input <= len(songs):
            print("now playing {}:{}".format(numb, name))
    break
