menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# for meal in menu:
#     if "spam" in meal:
#         meal.remove("spam")
#     print(meal)


for meal in menu:
    for dish in meal:
        if "spam" == dish:
            meal.remove(dish)
        if "spam" in meal:
            meal.remove("spam")
    print(", ".join(meal))
