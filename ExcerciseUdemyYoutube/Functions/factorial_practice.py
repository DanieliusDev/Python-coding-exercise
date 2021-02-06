# TODO here is practice assignment

def factorial(number: int) -> int:
    """
    Fuction that provides factorial of a number
    :param number:provide any full number from to
    :return: gets back the factorial of a number
    """
    for i in range(1, number):
        number = number * i
    return number


for i in range(0, 36):
    if i == 0:
        print("the numbers {0} factorial is: ".format(i) + str(i+1))
    elif i > 0:
        print("the numbers {0} factorial is: ".format(i) + str(factorial(i)))
