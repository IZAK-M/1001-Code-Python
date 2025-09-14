import sys
import random
from pyfiglet import Figlet, figlet_format

figlet = Figlet()

if len(sys.argv) == 2:
    sys.exit("Invalid usage")


if len(sys.argv) == 1:
    user_input = input("Input: ")

    polices = random.choice(figlet.getFonts())
    figlet.setFont(font=polices)
    print(figlet.renderText(user_input))

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    else:
        user_input = input("Input: ")
        print(figlet_format(user_input, font= sys.argv[2]))