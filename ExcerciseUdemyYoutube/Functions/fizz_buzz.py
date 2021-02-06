""" this is fizz buzz game for udemy"""
import file_list


def fizz_buzz_v1(number: int) -> str:
    """
    This program checks the given number and if it is divisible by 3 or 5 or none

    :param number: any number-that is integer
    :return: answer if it is or not divisible
    """
    if (number % 3) == (number % 5) == 0:
        return 'fizz buzz'
        # return number
    elif number % 5 == 0:
        return 'buzz'
        # return number
    elif number % 3 == 0:
        return 'fizz'
        # return number
    else:
        return str(number)
        # return int("1")


numbers_list = []
print("Yo sugar! find all the numbers from 1 to 33 ;) winky face")
user_input = input("Press ENTER to start the game!!!")
for i in range(1, 34):
    user_input = input("What's the number: ")
    print(fizz_buzz_v1(int(user_input)))
    if (int(user_input) % 3) and (int(user_input) % 5) >= 1:
        centered2 = "SORRY YOU LOST....".center(80)
        centered = "Hit Enter to EXIT game".center(80)
        exit_output = "********{0}********".format(centered)
        exit_output2 = "********{0}********".format(centered2)
        print(exit_output2)
        print(exit_output)
        input()
        break
    if user_input in numbers_list:
        print("***** Loser! You already used number {} ******".format(user_input).center(80))
        input("hit ENTER to EXIT")
        break
    if file_list.full_list == numbers_list:
        print("List is full")
        break
    numbers_list.append(user_input)
    print(numbers_list)

#
# for i in range(1, 101):
#     print(fizz_buzz(i))
