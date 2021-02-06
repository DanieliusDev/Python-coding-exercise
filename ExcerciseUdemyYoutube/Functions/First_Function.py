def perimeter(x, y, z):
    result = x * y / z
    return result


print(perimeter(10, 20, 5))


def calc_with_input():
    user_input = input("Please input 3 numbers:").split(",")
    numbers_list = []
    for number in user_input:
        numbers_list.append(int(number))
    result = numbers_list[0] * numbers_list[1] / numbers_list[2]
    return result


# print(calc_with_input())

def is_palindrome(string):
    return string[::-1].lower() == string.lower()


print(is_palindrome("Radar"))
