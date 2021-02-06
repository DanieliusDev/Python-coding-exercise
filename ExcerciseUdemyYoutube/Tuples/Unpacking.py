info = "Labukas saule, kaip pasportavai ?"

for index, char in enumerate(info):
    if char == "a":
        print(index, char)
    print(index, char)

# not really good example
table = "Coffee teable", 200, 100, 120
print(table[1] * table[2])

# easier and better example to understand with unpacking
name, length, high, width = table
print(name, high*length)
