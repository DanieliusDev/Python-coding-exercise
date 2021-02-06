# try except the errors so app doesnt break
try:
    bad_math = 10/0
    print(bad_math)
    number_one = input("First number : ")
    number_two = input("Second number : ")
    result = int(number_one) + int(number_two)
    print(result)
except ValueError:
    print("Wrong input")
except ZeroDivisionError:
    print("Nobody divide zero ok ?")
