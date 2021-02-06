# christmas gifting app
import random

gift_givers = ["Danielius", "Vilte", "Loreta", "Irena", "Agne", "Linas", "Aiste"]
user_has_santa = []

counter = 0
length = len(gift_givers)

while length >= counter:
    user_name = input("Hello, please tell me your name: ")
    if user_name in gift_givers:
        gift_givers.remove(user_name)
        random_receiver = random.choice(gift_givers)
        gift_givers.append(user_name)
        # user_has_santa.append(random_receiver)
        counter = counter + 1
        print(f"{user_name} will be secret santa of -> " + random_receiver)
        print(f"Counter is {counter}")


        # gift_givers.remove(random_receiver)

        # print(gift_givers)
        # print(user_has_santa)

        # gift_givers.remove(user_name)
        # random_user = random.choice(gift_givers)
        #
