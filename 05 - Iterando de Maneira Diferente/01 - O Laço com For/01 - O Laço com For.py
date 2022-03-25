print("*****************************")
print("Welcome to the Guessing Game!")
print("*****************************")

secret_number = 43

attempts = 3
# The "for" structure repeat the code according the specified range from the 1st parameter to the 2nd parameter
for round_number in range(1, attempts + 1):
    print("\nRound {} of {}".format(round_number, attempts))

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

print("Game Over")
