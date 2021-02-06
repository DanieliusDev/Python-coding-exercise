print("Hello Buyer of a new house!")

input_from_user = input("Would you like to buy a house? (Yes/No)")
price = 1_000_000

if input_from_user == "no":
    print(" Have a good day.")

if input_from_user == "yes":
    print("Nice")
    print("House costs " + str(price) + " Euro")
    input_from_user = input("so do you have a good credit score?")
    if input_from_user == "yes":
        print("Down payment will be 10%: " + str(price / 10) + " Euro")
    elif input_from_user == "no":
        print("Down payment will be: " + str(price / 5) + "Euro")

