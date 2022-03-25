print("*****************************")
print("Welcome to the Guessing Game!")
print("*****************************")

secret_number = 43

attempts = 3
for round_number in range(1, attempts + 1):
    print("\nRound {} of {}".format(round_number, attempts))

    kick = input("Write the secret number: ")
    print("You kick the number", kick)

    kick = int(kick)

    if kick < 1 or kick > 100:
        print("You must enter a number between 1 at 100!")

        continue

    if kick == secret_number:
        print("You're right!")

        break
    else:
        print("You missed!")

        if kick > secret_number:
            print("Your kick is greater than secret number")
        elif kick < secret_number:
            print("Your kick is less than secret number")

print("Game Over")
