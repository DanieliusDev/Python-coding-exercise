# name and age inout required

name = input("What is your name? ")
age = input("What is your age? ")

if 18 <= int(age) < 31:
    print(f"Welcome to the holiday {name}")
else:
    print(f"hey {name} Entrance not allowed. ")
