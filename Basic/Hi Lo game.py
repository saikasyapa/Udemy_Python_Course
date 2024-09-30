low = 1
high = 1000

print(f"Please think of the number between {low} and {high}")
input("Press Enter to start")

guesses = 1
while True:
    print(f"Calculating range is {low} to {high} ")
    guess = low+(high - low) // 2
    high_low = (input(f"my guess is {guess}.Should i guess higher or lower? "
                      "Enter h or l, or c if my guess is correct").casefold())

    if high_low == "h":
        low = guess + 1

    elif high_low == "l":
        high = guess - 1

    elif high_low == "c":
        print(f"I got it in {guesses} guesses")
    else:
        print("Please enter h,l or c")

    guesses = guesses +1


