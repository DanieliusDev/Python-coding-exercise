#  first 0 is begining, 100 is endpoint not included, 7 is divisible or to print every 7 th number
for i in range(0, 100, 7):
    if i > 0 and i % 11 == 0:
        print(i)
        break
    else:
        print(i)
print("_" * 50)

# if i want to skip some sort of item
present_list = ["xbox", "watch", "ssd", "underwear"]

for item in present_list:
    if item == "underwear":
        continue
    print("I want " + item)
print("-" * 100)

for i in range(0, 20):
    if (i % 3) and (i % 5) and (i != 0):
        print(i)  # TODO well this is new to me
