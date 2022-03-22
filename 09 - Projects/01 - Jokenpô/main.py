from random import randint
from time import sleep


def __main__():
    print("Welcome to the JoKenPô!!!")
    print("-" * 50)

    pc = randint(1, 3)
    user = int(input("""What's your move?
(1) - Scissor
(2) - Stone
(3) - Paper
-> """))

    print("\nJO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PÔ\n")
    sleep(0.5)

    plays = ["Scissor", "Stone", "Paper"]
    print("PC move {}\n".format(plays[pc - 1]))

    if pc == user:
        print("Tied game!")

    elif user == 1:
        if pc == 2:
            print("PC Won!")
        else:
            print("User Won!")

    elif user == 2:
        if pc == 1:
            print("User Won!")
        else:
            print("PC Won!")

    elif user == 3:
        if pc == 1:
            print("PC Won!")
        else:
            print("User Won!")


if __name__ == "__main__":
    __main__()
