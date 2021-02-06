secret_word = "money"

guess = ""
guess_count = 1
guess_limit = 4
out_of_guesses = False
while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter a guess: ")
        guess_count += 1

    else:
        out_of_guesses = True
        print("you lost")

if out_of_guesses:
    print("no more attemps left...")
else:
    print("You won!!")
