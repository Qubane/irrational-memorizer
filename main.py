"""
Main file
"""

import os


CONSTANTS_PATH: str = "constants"
CONSTANTS: list[dict[str, str]] = [
    {
        "filename": "pi.txt",
        "name": "Pi constant",
        "variable": "PI",
        "preview": "3.1415"
    },
    {
        "filename": "e.txt",
        "name": "Euler\'s constant",
        "variable": "e",
        "preview": "2.7182"
    },
    {
        "filename": "sqrt(2).txt",
        "name": "Square Root of 2",
        "variable": "SQRT 2",
        "preview": "1.4142"
    },
    {
        "filename": "golden ratio.txt",
        "name": "Golden ratio",
        "variable": "PHI",
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
    constant = CONSTANTS[user_input - 1]
    print(f"{f'[ You chose {constant['name']} ]':=^90}")
    print(f"{f'[ press [CTRL + C] at any moment to exit ]':=^90}")
    input("> press [ENTER] to continue...")

    # clear
    clear()

    # enter a loop
    slice_size = 4
    current_slice = ""
    with open(f"{CONSTANTS_PATH}/{constant['filename']}", "r", encoding="ascii") as file:
        while True:
            # print out record
            print(f"{f'[ Current record is {slice_size - 2} digits! ]':=^90}")

            # reset current slice
            current_slice = ""

            # generate constant output
            output = f"| {constant['variable']} = "
            output_indent = len(output) - 1
            output_length_offset = 0
            for idx, digit in enumerate(file.read(slice_size)):
                # add digit
                output += digit
                current_slice += digit

                # check if there's enough space
                if len(output) - output_length_offset >= 84:
                    # add encasing at the end
                    output += f"{' ' * (90 - len(output) + output_length_offset - 1)}|\n|{' ' * output_indent}"
                    output_length_offset = len(output) - output_indent - 1
                    continue

                # add space every 2 digits
                if (idx - 1) % 2 == 0:
                    output += " "

            # make sure to go to the start of the file
            file.seek(0)

            # add encasing at the end
            output += f"{' ' * (90 - len(output) + output_length_offset - 1)}|"

            # print out the output
            print(output)

            # print ask for input
            print("=" * 90)
            input("> press [ENTER] when you are ready")

            # clear
            clear()

            # Ask to repeat the digits
            print(f"{f'[ Now enter the constant ]':=^90}")
            user_constant = input("> ")

            # if user_constant is not equal to current_slice -> exit
            if user_constant != current_slice:
                break

            # otherwise progress forward by 2
            slice_size += 2

    # :(
    print(f"{f'[ Sorry! You lost :< ]':=^90}")
    print(f"{f'[ Record was {slice_size - 2} digits! ]':=^90}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
