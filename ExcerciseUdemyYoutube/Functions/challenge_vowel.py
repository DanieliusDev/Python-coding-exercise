text = set("Today was better then yesterday, however not as good as tomorrow will be!")
vowels = "aeiou"


def remove_vowels():
    for letter in vowels:
        if letter in text:
            text.remove(letter)
    return sorted(text)


print(remove_vowels())
