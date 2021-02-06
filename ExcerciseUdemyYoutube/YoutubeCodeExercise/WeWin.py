parrot = "Norwegian Blue"

print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print(parrot[10:14])

abc = "abcdefghijklmnopqrstuvwxyz"
print(abc[3] + abc[0] + abc[13])

number = "1,457,456,874/123;715"
separators = number[1::4]

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

reverse = abc[::-1]
print(reverse)

print(reverse[9:12])
print(reverse[-5:])
print(abc[-8:])

print(abc[4::-1])

print("abc" in abc)  # true
print("dan" in abc)  # false
