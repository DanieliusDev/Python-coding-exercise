# Passed 3 numbers all added
def sum_numbers(*digits: float) -> float:
    """
    calculate sum
    :param digits: you can provide any number of digits which will be added
    :return: the sum of every digit
    """
    result = 0
    for digit in digits:
        result += digit
    return result


print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
print(sum_numbers(10, 15, 11))
