"""
Main file
"""

import os


CONSTANTS_PATH: str = "constants"
CONSTANTS: list[dict[str, str]] = [
    {
        "filename": "pi.txt",
        "name": "Pi constant",
        "preview": "3.1415"
    },
    {
        "filename": "e.txt",
        "name": "Euler\'s constant",
        "preview": "2.7182"
    },
    {
        "filename": "sqrt(2).txt",
        "name": "Square Root of 2",
        "preview": "1.4142"
    },
    {
        "filename": "golden ratio.txt",
        "name": "Golden ratio",
        "preview": "1.6180"
    }
]


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    # initialize with 0
    user_input = 0

    # pretty print magic numbers
    max_number_length = len(str(len(CONSTANTS)))
    max_name_length = max(len(x["name"]) for x in CONSTANTS)

    # print welcome message
    print(f"{'[ Welcome to the very cool irrational number memorizer ]':=^90}")
    while True:
        # output all constant options
        for idx, constant in enumerate(CONSTANTS):
            message = (f"| [ {idx + 1: >{max_number_length}} ] "
                       f"{constant['name']: <{max_name_length}} "
                       f"| {constant['preview']}...")
            print(f"{message: <88} |")

        # print input message
        print(f"{f'| [ 0 ] Exit': <88} |")
        print(f"{'[ choose one of the irrational numbers ]':=^90}")

        # ask for input
        try:
            user_input = int(input("> "))
        except ValueError:
            continue

        # if input within range -> break
        if -1 < user_input <= len(CONSTANTS):
            break

    # if exit -> exit
    if user_input == 0:
        return

    # if one of the constants
    print(f"{f'[ You chose {CONSTANTS[user_input - 1]['name']} ]':=^90}")
    print(f"{f'[ press [CTRL + C] at any moment to exit ]':=^90}")
    input("> press [ENTER] to continue...")

    # enter a loop
    slice_size = 2
    with open(CONSTANTS[user_input - 1]['filename'])
    while True:
        print("")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
