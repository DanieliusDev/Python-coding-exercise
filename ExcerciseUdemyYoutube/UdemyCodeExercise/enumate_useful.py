gift_list = ["xbox", "watch", "clothes", "ssd", "headphones", "earpods"]
choice = ""
my_gift_list = []
print(gift_list)

for index, gift in enumerate(gift_list):

    choice = input("Hey choose what gift you want: ")

    print("{}. is {}".format(index + 1, gift))

    if choice in "123456":
        print("You chose {} which is {}".format(choice, gift))
        my_gift_list.append(gift)
        print(my_gift_list)
