import random

# todo Please look over this as it is not your Dan, but udemy code. LEARN FROM THIS

needs_gifts = ["Danielius", "Vilte", "Loreta", "Irena", "Agne", "Linas", "Aiste"]
needs_recipients = ["Danielius", "Vilte", "Loreta", "Irena", "Agne", "Linas", "Aiste"]
gift_dict = dict()

for giver in needs_recipients:
    giftee_pool = needs_gifts.copy()
    if giver in giftee_pool:
        giftee_pool.remove(giver)
    giftee = random.choice(giftee_pool)
    needs_gifts.remove(giftee)
    gift_dict[giver] = giftee

for giver, recipient in gift_dict.items():
    print(f"{giver} is giving a gift to {recipient}.")
