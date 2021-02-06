premade_text = ["{} times {} is {}"]


def appending():
    with open('cities.txt', 'a') as text_file:
        for i in range(1, 13):
            for j in range(1, 13):
                for text in premade_text:
                    result = i * j
                    text_file.write('\n' + text.format(i, j, result))
            print("\n" + "-" * 30, file=text_file)
        return text_file


appending()
