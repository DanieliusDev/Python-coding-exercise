# action_list = ["Drink coffee", "Learn python", "Play xbox", "Have sex", "Take a nap", "Make food", "Workout", "Exit"]
#
#
# def reading():
#     for action in action_list:
#         print("1." + action)
#
#
# reading()
# print("-" * 100)
# while True:
#
#     chosen_action = input("Hello, what would you like to do now? ")
#     if chosen_action == "Exit".casefold():
#         print("The tasks are over.")
#         break
#     if chosen_action in action_list:
#         print("So it shall be - {}".format(chosen_action))
#     elif chosen_action not in action_list:
#         print("-" * 100)
#         print(f"Sorry this is no on the list - {chosen_action}")
#         print(f"Choose one of the following:")
#         reading()

second_action_list = ["1.Have Sex", "2.Workout", "3.Eat food", "4.Nap", "5.Play xbox", "6.Shop", "7.Have fun outside",
                      "0.Exit"]


def todo():
    for actions_todo in second_action_list:
        print(actions_todo)


todo()
while True:
    user_input = input("What it will be today and now? ")
    if user_input == "0":
        print("Game Over")
        break
    elif user_input not in second_action_list:
        print("Choose one of the below: ")
        todo()
        print("-" * 100)
    for action in second_action_list:
        if action.startswith(user_input):
            print("So it will be " + action)
