# This one will allow to access external files in same directory

# there can be "r" or "w" or "a" for reading writing and appending
# "r" for reading only
# "w" for overwriting file, also can be used to create new file
# "a" for adding text or so
question_list = open("seb procurement part 2.txt", "w")
# print(question_list.read())
# for questions in question_list:
#     print(questions.__add__("-" * 50))
#     print(questions.__contains__("diena"))
#     for symbols in questions:
#         print(symbols)

question_list.write("I sita pozicija neprieme :/")
question_list.write("\nCareful with appending, if you run app again, it will add everything one more time :(")
question_list.close()
