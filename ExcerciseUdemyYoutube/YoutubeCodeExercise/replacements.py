age = 26
greeting = "Hello my age is: "
print(greeting + str(age))

print(greeting + "{0}".format(age))
print()

birth_year = input("What is your birth year: ")

years_old = (2020 - int(birth_year))

print("You are: {0} years old".format(years_old))
