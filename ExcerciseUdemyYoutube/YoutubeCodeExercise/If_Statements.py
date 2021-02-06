name = input("Hey! What is your name? -")
print(f"Hello {name} it is nice to meet you!")
age = int(input("and how old are you? -"))
print(f"Ahh so your name is {name} and you are {age} years old")

print()

if age >= 18:
    print(f"So you are {age} and you are old enough to vote!!")
else:
    print(f"Sorry, you are only {age} so please grow up first, then come back to vote")

