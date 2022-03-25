print("*****************************")
print("Welcome to the Guessing Game!")
print("*****************************")

secret_number = 43

kick = input("Write the secret number: ")

print("You kick the number", kick)

kick = int(kick)

if kick == secret_number:
    print("You're right!")
else:
    print("You missed!")

    if kick > secret_number:
        print("Your kick is greater than secret number")
    # If the first condition above is false, the "elif" verify if the second condition is true, executing the block code
    elif kick < secret_number:
        print("Your kick is less than secret number")

print("Game Over")
