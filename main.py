"""
Main file
"""


def main():
    # initialize with 0
    user_input = 0

    # print welcome message
    print(f"{'[ Welcome to the very cool irrational number memorizer ]':=^90}")
    while True:
        # print input message
        print(f" {'[ 1 ] Pi constant': <24} | 3.1415...")
        print(f" {'[ 2 ] Euler\'s constant': <24} | 2.7182...")
        print(f" {'[ 3 ] square root of 2': <24} | 1.4142...")
        print(f" {'[ 4 ] Golden ratio': <24} | 1.6180...")
        print(f" [ 0 ] Exit")
        print(f"{'[ choose one of the irrational numbers ]':=^90}")

        # ask for input
        try:
            user_input = int(input("> "))
        except ValueError:
            continue

        # if input within range -> break
        if -1 < user_input <= 4:
            break

    # if exit -> exit
    if user_input == 0:
        return


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
