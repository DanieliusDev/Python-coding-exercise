# This will be "Language editor" practice
phrase = input("Whats the text: ")


def editor(phrase):
    edit = ""
    for letter in phrase:
        if letter in "dD":
            edit = edit + "b"
        else:
            edit = edit + letter
    return edit


print(editor(phrase))
