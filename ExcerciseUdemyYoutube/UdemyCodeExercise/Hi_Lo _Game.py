low = 1
high = 1000

print("Please think up of a number between {} and {}, for me to guess it!".format(low, high))
input("Please hit ENTER to continue when your ready.")

guesses = 1

while True:
    guess = low + (high - low) // 2
    high_low = input("So my guess is {}. Should I guess lower or higher?"
                     "Enter l for low, or h for high, or c for correct: "
                     .format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter l or h or c: ")
    guesses = guesses + 1
