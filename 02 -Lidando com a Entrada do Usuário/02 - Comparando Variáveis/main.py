print("*****************************")
print("Welcome to the Guessing Game!")
print("*****************************")

secret_number = 43

# The "input()" read the input of user in keyboard
kick = input("Write the secret number: ")

print("You kick the number", kick)

# The "int()" converts a variable to type "int"
kick = int(kick)

# The "if" verify the condition between the "()" and execute the code inside the block if it is true
if kick == secret_number:
    # The "TAB" represents a block of code inside other structure of code
    # This TAB below represents that "print("You Win!")" is inside "if(kick == secret_number):"
    print("You Win!")
else:
    print("You Lose!")

print("Game Over")
