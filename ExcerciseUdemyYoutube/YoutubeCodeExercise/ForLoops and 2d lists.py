chores_to_do = ["buy TV", "buy groceries", "cook food", "study python"]

# this one will loop and print lists indexes and first letter of every index
for tasks in chores_to_do:
    print(tasks)
    print(tasks[0])
print("*" * 50)

# this one is nested loop which will loop every letter, one by one from top to bottom
for new_task in chores_to_do:
    for letter in new_task:
        print(letter)
    print("")
    print("-" * 50)

# this is 2d list
todo_list = [
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [9, 8, 7, 6],
    [0]
]

# Again nested for loop takes out every number within every list in 2d list
print(todo_list)
for every_list in todo_list:
    print(every_list)
    for every_number in every_list:
        print(every_number)
