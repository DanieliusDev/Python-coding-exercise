import random
from banner_function_docstrings import banner
from coloured_text import colour_text, MAGENTA, RED

banner("Hello Sugar! :*", 80)
banner("Today is the lucky day where you will be challenged ;)")
banner("Best of luck!!!")

user_input = input("Hit ENTER to start game!")
counter = 0
while user_input != "0":

    def fizz_buzz_word_game() -> str:
        random_number = random.randint(1, 51)
        print(random_number)
        user_input = input("fizz(3), buzz(5), fizz buzz(3 and 5) or none ? ")

        if (random_number % 3) == (random_number % 5) == 0 and user_input == "35":
            return 'Correct it was FIZZ BUZZ'
        elif random_number % 5 == 0 and user_input == "5":
            return 'Correct it was BUZZ'
        elif random_number % 3 == 0 and user_input == "3":
            return 'Correct it was FIZZ'
        elif (random_number % 3) and (random_number % 5) >= 1 and user_input == "1":
            return "Correct"
        else:
            print("Sorry you failed :(")
            print("*" * 20 + "  Your FINAL SCORE is : {0}  ".format(counter) + "*" * 20)
            input("Hit ENTER to exit")
            exit()


    # TODO add final score and force to use fizz buzz same time

    print(fizz_buzz_word_game())
    counter = counter + 1
    colour_text("*" * 20 + "  Your score is : {0}  ".format(counter) + "*" * 20, RED)
    # print("*" * 20 + "  Your score is : {0}  ".format(counter) + "*" * 20)
