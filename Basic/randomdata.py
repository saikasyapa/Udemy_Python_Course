# import random
# answer = random.randint(1,10)
# guess = int(input("Please guess the number from 1 to 10 : "))
#
# if guess == answer:
#     print("Hoorah,Well done")
# else:
#     if guess < answer:
#         print("Try  higher number")
#     else:
#         print("try lower value")
#     guess = int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#         print("No luck")
#
#
# print(guess)


# import random
# answer = random.randint(1,10)
# guess = int(input("Enter your gussing in between 1 to 10"))
#
# if guess == answer:
#     print("Well done Your guessing is correct")
# elif guess > answer:
#     print("Please try lower number")
#     guess = int(input())
#     if guess == answer:
#         print("Wll done")
#     else:
#         print("try your luck next time")
# elif guess < answer:
#     print("Please try higher value")
#     guess = int(input())
#     if guess == answer:
#         print("Well done")
#     else:
#         print("Try your luck next time")

# import random
# answer = random.randint(1,10)
#
#
#
# while True:
#     guess = int(input("Enter your guss in between 1 to 10 numbers : "))
#     if guess == answer:
#         print("fnnd")
#         break
#     else:
#         print("bdhd")

# import random
# answer = random.randint(1,10)
# guess = int(input("Enter your guss in between 1 to 10 numbers : "))
#
#
#
# while guess != answer:
#
#     if guess ==0:
#         print("Ian Done")
#         break
#     elif guess < answer:
#         print("Your guess is too low")
#     else:
#         print("Your Guess is too high")
#     guess = int(input("Try again or enter 0 to quit :"))
#
# print("Ok Well done Good Job")

import random
answer = random.randint(1,10)
guesses = []
guess = int(input("Enter your guss in between 1 to 10 numbers : "))



while guess != answer:

    if guess ==0:
        print("Ian Done")
        break
    guesses.append(guess)
    if guess < answer:
        print("Your guess is too low")
    else:
        print("Your Guess is too high")
    guess = int(input("Try again or enter 0 to quit :"))

if guess == answer:
    guesses.append(guess)
    print(f"Well done! You guessed the correct answer, Your guesses are:{guesses}")










