# tree1 = "Oak"
#
# tree2 = "Maple"
#
# if tree1 == tree2:
#     print("The trees are the same")
# else:
#     print("The trees are different")
#
# x = 5
# y = 7
#
# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is smaller than y")
# else:
#     print("x equals y")
#

answer = 7
print("Guess the number")
guess = int(input())

# if guess == answer:
#     print("You are correct")
# else:
#     print("Please guess again")
#     guess = int(input())
#     if guess > answer:
#         print("Please guess lower")
#     elif guess < answer:
#         print("Please guess higher")
#     elif guess == answer:
#         print("Correct!")
#     else:
#         print("You failed")

if guess == answer:
    print("YES!")
else:
    print("Guess again: ")
    guess = int(input())
if guess == answer:
    print("Correct")
else:
    print("No.")
