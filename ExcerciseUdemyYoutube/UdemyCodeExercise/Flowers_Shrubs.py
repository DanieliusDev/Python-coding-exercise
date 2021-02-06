data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# write your code here.


# more agile/versatile/better code
flowers = []
shrubs = []
# choice = ""
#
# while choice != 0:
#     choice = input("Hey, which flower type should be sorted: ")
#     print("_" * 500)
#     for single_flower in data:
#         if choice in single_flower:
#             flowers.append(single_flower)
#         elif choice in single_flower:
#             shrubs.append(single_flower)
#     print(flowers)


# poor primitive code
for single_flower in data:
    if "Flower" in single_flower:
        flowers.append(single_flower)
    elif "Shrub" in single_flower:
        shrubs.append(single_flower)
print(shrubs)
print(flowers)
