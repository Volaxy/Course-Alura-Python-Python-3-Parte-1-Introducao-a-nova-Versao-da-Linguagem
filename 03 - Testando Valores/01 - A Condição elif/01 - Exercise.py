age_str = input("Write your age: ")
age = int(age_str)

if age > 18:
    print("You are of legal age.")
else:
    if age < 12:
        print("You are a kid.")
    elif age > 12:
        print("You are a teenager.")
