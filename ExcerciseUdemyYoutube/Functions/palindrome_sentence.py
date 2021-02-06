sentence1 = "Was it a car or a cat i saw?"
sentence2 = "Do geese see god?"
sentence3 = "Desnes not far, Rafton, sensed"
sentence4 = "LOL, no, lol"


def is_a_palindrome(string):
    return string[::-1].lower() == string.lower()


def remove_all_between_words(string):
    new_sentence = string.split()
    get_rid_of_else = "".join(new_sentence)
    get_rid_of_else = get_rid_of_else.split(",")
    value = "".join(get_rid_of_else).removesuffix("?")
    return value


def is_palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return "".join(string)


print(is_a_palindrome(remove_all_between_words(sentence1)))
print(is_palindrome_sentence(sentence1))
