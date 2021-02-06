user_input = input("Please enter three numbers: ").split(",")

integer_list = []

for numbers in user_input:
    integer_list.append(int(numbers))

result = integer_list[0] + integer_list[1] + integer_list[2]
print(result)
