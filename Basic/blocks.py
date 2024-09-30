name = input("Enter your name")
age = int(input(f"Enter your age {name} "))


if age >= 18:
    print("You are eligible to vote")
else:
    print(f"Please comback after {18-age} Years")