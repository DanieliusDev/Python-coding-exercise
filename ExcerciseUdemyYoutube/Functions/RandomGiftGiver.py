import random

family_list_givers = ["Danielius", "Vilte", "Loreta", "Irena", "Agne", "Linas", "Aiste"]
family_list_receivers = []

while len(family_list_givers) != 0:
    input("Hit enter to know who gives gifts to who :)!")
    for name in family_list_givers:
        random_giver = random.choice(family_list_givers)
        random_receiver = random.choice(family_list_givers)
        print(random_giver + " is Santa of: " + random_receiver)
    print("-" * 50)
