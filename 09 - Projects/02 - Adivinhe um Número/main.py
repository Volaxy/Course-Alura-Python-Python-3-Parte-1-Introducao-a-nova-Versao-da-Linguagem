from random import random


secret_number = int(random() * 100)
chances = 5
end_game = False

while not end_game:
    print("\nRemaining chances:", chances)
    number = int(input("Enter a number: "))

    if number == secret_number:
        print("You \033[32mWon!\033[30m")

        end_game = True
    else:
        chances -= 1
        if chances == 0:
            end_game = True

        print("You \033[31mFail!\033[30m")

        if number < secret_number:
            print("Your kick was lower than the secret number")
        else:
            print("Your kick was bigger than the secret number")
