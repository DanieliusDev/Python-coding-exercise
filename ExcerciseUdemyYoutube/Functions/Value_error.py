# Max should be 200 of one number otherwise will give error


def sum_of_two(a, b):
    """
    Gets two numbers returns sum of them, not allowed for one of the a
    or b to be over 200 else gives ValueError

    :param a: first number
    :param b: second number
    :return: returns a sum of first and second number in other words a + b = sum
    """
    result = a + b

    if a and b > 200:
        raise ValueError("These were too high {0} and {1}"
                         .format(a, b))
    return result


print(sum_of_two(50, 200))
