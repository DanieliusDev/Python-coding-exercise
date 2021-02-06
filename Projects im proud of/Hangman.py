import random
import webbrowser

list_of_words = ['work', 'holiday', 'dinner', 'vacation']

# TODO list:
#  make counter, - DONE
#  draw hangman, - DONE
#  make 6 lives, - DONE
#  print how much letters in word, - DONE
#  print correct letters in word instead of underscores, - DONE
#  next part would be to make an GUI and put hangman in it ;)
BEGIN = 0
END = len(list_of_words) - 1
AMOUNT_OF_MOVES = 7


# TODO This is a fully working hangman game instructions for game are in
#  the game itself


def guessing_game():
    """
    This is my first not so bad looking hangman game
    which does not take anything and does not return anything
    :return: retuns fun
    """
    print("Games rules are simple, this is a hangman."
          "\nGuess letters correctly and the guy will live."
          "\nMake mistakes and kaput for the little guy."
          "\nYou will get 6 tries so you know and if you wish quit hit 0.")
    input('Hit any button to start game and GOOD LUCK!')
    print()
    # this generates a random word below
    random_word = list_of_words[random.randint(BEGIN, END)]
    print(random_word)
    # counter is for controlling the amount of moves is made
    counter = 0
    # this is for creating underlines of as many letters the word is
    underlines = ['_'] * len(random_word)
    # will print amount of letters in a word
    print("Word contains {} letters".format(len(random_word)))
    list_of_used_letters = ''
    while True:
        letter = input("Guess letter: ")
        # if user will enter 0 game will exit
        if letter == '0':
            break
        if letter in list_of_used_letters:
            # this if statement is meant for duplicate letters to not be used
            print("sorry such letter already exists")
            continue
        # below for loop will index every letter i = x from the random word
        # if statement for checking if input was the letter in the word
        for i, x in enumerate(random_word):
            if x is letter:
                underlines[i] += letter
        # this print line is meant for joining all the _ and if guess was
        # correct to add letter in the correct place
        print(''.join([str(x) + ' ' for x in underlines]))
        # in below we add used letters to variable so duplicates would
        # not be used
        list_of_used_letters += letter
        # once all the letters are guessed below if statement
        # will open web page with provided link as prize :)
        if '_' not in underlines:
            webbrowser.open('https://www.youtube.com/watch?v=ZyhrYis509A')
            print('Did you like your prize?')
            input('Hit any button to exit')
            break
        # below if and elif statements are for printing the hangman
        # and if it was correct letter/guess or not
        if letter in random_word:
            print('Correct! There is such letter {}'.format(letter))
        elif letter not in random_word and counter == 0:
            counter += 1
            print("Sorry, you missed! {} tries left".format(AMOUNT_OF_MOVES - counter))
            print('-------'
                  '\n|      '   '|'
                  '\n|      '
                  '\n|     '
                  '\n|     '
                  '\n|      '
                  '\n---')
            print(''.join([str(x) + ' ' for x in underlines]))

            print('*' * 100)
        elif letter not in random_word and counter == 1:
            counter += 1
            print("Sorry, you missed! {} tries left".format(AMOUNT_OF_MOVES - counter))
            print('-------'
                  '\n|      '   '|'
                  '\n|      '   'o'
                  '\n|     '
                  '\n|     '
                  '\n|      '
                  '\n---')
            print(''.join([str(x) + ' ' for x in underlines]))

        elif letter not in random_word and counter == 2:
            counter += 1
            print("Sorry, you missed! {} tries left".format(AMOUNT_OF_MOVES - counter))
            print('-------'
                  '\n|      '   '|'
                  '\n|      '   'o'
                  '\n|     '    '|'
                  '\n|     '
                  '\n|      '
                  '\n---')
            print(''.join([str(x) + ' ' for x in underlines]))

        elif letter not in random_word and counter == 3:
            counter += 1
            print("Sorry, you missed! {} tries left".format(AMOUNT_OF_MOVES - counter))
            print('-------'
                  '\n|      '   '|'
                  '\n|      '   'o'
                  '\n|     ' '/''|'
                  '\n|     '
                  '\n|      '
                  '\n---')
            print(''.join([str(x) + ' ' for x in underlines]))

        elif letter not in random_word and counter == 4:
            counter += 1
            print("Sorry, you missed! {} tries left".format(AMOUNT_OF_MOVES - counter))
            print('-------'
                  '\n|      '   '|'
                  '\n|      '   'o'
                  '\n|     ' '/''|''\\'
                  '\n|     '
                  '\n|      '
                  '\n---')
            print(''.join([str(x) + ' ' for x in underlines]))

        elif letter not in random_word and counter == 5:
            counter += 1
            print("Sorry, you missed! {} tries left".format(AMOUNT_OF_MOVES - counter))
            print('-------'
                  '\n|      '   '|'
                  '\n|      '   'o'
                  '\n|     ' '/''|''\\'
                  '\n|     '   '/'
                  '\n|      '
                  '\n---')
            print(''.join([str(x) + ' ' for x in underlines]))

        elif letter not in random_word and counter == 6:
            counter += 1
            print(''.join([str(x) + ' ' for x in underlines]))

            print("Sorry, you missed! {} tries left".format(AMOUNT_OF_MOVES - counter))
            print('-------'
                  '\n|      '   '|'
                  '\n|      '   'o'
                  '\n|     ' '/''|''\\'
                  '\n|     '   '/ \\'
                  '\n|      '
                  '\n---')
            print('GAME OVER')
            input('Hit any button to EXIT')
            break


guessing_game()

# TODO implement this change in hangman code, analyze this code PLEASE!
# def change_underlines(word):
#     output = ['_'] * len(word)
#
#     def print_output():
#         print(''.join([str(x) + " " for x in output]))
#
#     while True:
#         print_output()
#         letter = input("Guess letter: ")
#         for i, x in enumerate(word):
#             if x is letter:
#                 output[i] += letter

# change_underlines('Daniel')
