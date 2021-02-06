for i in range(1, 15):
    print("{0:2} is squared {1:3} same number is cubed {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 15):
    print("{0:2} is squared {1:<3} same number is cubed {2:^4}".format(i, i ** 2, i ** 3))
    print("*"*50)

age = 24
# f strings is nice
print(f"Daniel is {age} years old")

print(f"Daniel is {1994 - 2020:10} years old")
