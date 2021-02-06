import math
import random


# computer_sign = ["s" or 'scissors', "r" or "rock", "p" or "paper"]
# user_input = input("Please choose your sign s or r or p ?")
# print(computer_sign)
#
# if user_input == "s":
#
#     print("nice")
# else:
#     print("not nice")


def play():
    user_input = input("What is your sign? 'r' for rock, 'p' for paper, and 's' for scissors \n")
    user_input = user_input.lower()

    computer_input = random.choice(['r', 'p', 's'])

    if user_input == computer_input:
        return 0, user_input, computer_input
    return -1, user_input, computer_input

    if is_win(user_input, computer_input):
        return 1, user_input, computer_input
    return -1, user_input, computer_input


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True
    return False


def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n / 2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user_input, computer_input = play()
        if result == 0:
            return "It's a TIE!!! You chose {}, PC chose {}".format(user_input, computer_input)
        elif result == 1:
            player_wins += 1
            print("You WON!!! You had {} and PC had {}".format(user_input, computer_input))
        else:
            computer_wins += 1
            print("Loser, You had {} and PC had {}".format(user_input, computer_input))
    if player_wins > computer_wins:
        print("CHAMP")
    else:
        print("Meh, too bad.")


if __name__ == "__main__":
    play_best_of(3)
    play_best_of(9)
