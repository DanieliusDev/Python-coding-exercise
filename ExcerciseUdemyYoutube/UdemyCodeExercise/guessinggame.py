import random

lowest = 0
highest = 10
answer = random.randint(lowest, highest)
# print(answer)  # TODO: Remove after testing
counter_of_guesses = 0
print("Please guess number between 1 and {}: ".format(highest))
guess = 0


def get_int(prompt):
    while True:
        choice = input(prompt)
        if choice.isnumeric():
            return int(choice)
        else:
            print("{0} That aint number".format(choice))


while guess != answer:
    guess = get_int(": ")

    if guess != 0:
        counter_of_guesses += 1
        print("So far there was {} guesses".format(counter_of_guesses))
    else:
        print("Game exit!")
        break
    if guess == answer:
        print("You got it first time")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
        # guess = get_int(": ")
        if guess == answer:
            print("Well done, you guessed it")
            print("Total were {} guesses".format(counter_of_guesses))

        # else:
        # print("Sorry, you have not guessed correctly")
