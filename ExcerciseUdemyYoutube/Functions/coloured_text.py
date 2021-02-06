import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_text(text: str, colour: str) -> None:
    output_string = "{}{}{}".format(colour, text, RESET)
    print(output_string)


colorama.init()
colour_text("This will be new experience with colours so Magenta!", MAGENTA)
colorama.deinit()
