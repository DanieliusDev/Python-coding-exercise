# In here we have provided first and second argument with default values

def banner(text=" ", screen_width=80):
    """
    prints out texted centered within given 'width'

    :param text: Pass down desired text which will be centered
    :param screen_width: pass down desired width and make sure it's longer than text
    :raises ValueError: if value of one of the numbers is more then 200
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} too long, larger then specified {1}")
        # print("Oh no!")
        # print("Text was too long for this app")
    if text == "*":
        print("*" * screen_width)
    else:
        centered = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered)
        print(output_string)

#
# print("*" * 100)
# print(banner.__doc__)
# print("*" * 100)
# help(banner)
# banner("Daniel")
# banner()
# banner("Vilte", 78)
# # Here below we only used width without first argument
# banner(screen_width=76)


