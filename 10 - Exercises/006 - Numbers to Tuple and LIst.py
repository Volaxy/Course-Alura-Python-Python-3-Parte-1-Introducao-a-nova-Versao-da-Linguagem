numbers = input("Write the numbers separate by ,: ")
print("Numbers:", numbers)

numbers = numbers.replace(",", "','")
print("List: [" + numbers, end="]\n")
print("Tuple: (" + numbers, end=")")
