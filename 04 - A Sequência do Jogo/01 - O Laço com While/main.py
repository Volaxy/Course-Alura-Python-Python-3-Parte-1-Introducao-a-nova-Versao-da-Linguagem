print("*****************************")
print("Welcome to the Guessing Game!")
print("*****************************")

secret_number = 43

round_number = 1
attempts = 3
while round_number <= attempts:
    print("\nRound", round_number, "of", attempts)
    kick = input("Write the secret number: ")

    print("You kick the number", kick)

    kick = int(kick)

    if kick == secret_number:
        print("You're right!")
    else:
        print("You missed!")

        if kick > secret_number:
            print("Your kick is greater than secret number")
        elif kick < secret_number:
            print("Your kick is less than secret number")

    round_number += 1

print("Game Over")
