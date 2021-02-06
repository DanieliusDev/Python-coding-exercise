data = [111, 444, 555, 888, 412, 647, 951,
        789, 654, 258, 5, 4, 234,
        543, 345, 123235245, 213,
        435, 2334, 345
        ]

min_valid_amount = 200
max_valid_amount = 400

for index in range(len(data) - 1, -1, -1):
    if data[index] > max_valid_amount or data[index] < min_valid_amount:
        print(index, data)
        del data[index]
print(data)

# another backwards/reverse way

top_index = len(data) - 1
for index, number in enumerate(reversed(data)):
    if number < min_valid_amount or number > min_valid_amount:
        print(top_index - index, number)
        del data[top_index - index]
print(data)
