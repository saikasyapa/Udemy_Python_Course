low = 1
high = 1000
print(f"Please think of a number between ")
input("Enter to start")

# guesses = 1
while low != high:
    # print(f"Guessing the range in {low} to {high}")
    guess = low + (high - low) // 2
    high_low = input(f"my guess is {guess}.should i guess higher or lower? "
                     "Enter h or l, or c if my guess is correct").casefold()

    if high_low == "h":
        low = guess +1
    elif high_low == "l":
        high = guess -1
    # elif high_low == "c":
    #     print(f"I got it in {guesses}")
    #     break
    # else:
    #     print("Please enter h,l or c")

    # guesses = guesses + 1
else:
    print(f"You thought of the number {low} ")
    # print(f"I got it in {guesses}")



