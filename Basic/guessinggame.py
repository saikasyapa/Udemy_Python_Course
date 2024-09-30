# answer = 5
#
# guess = int(input('Guess the number from 1 to 10 :'))
# print(guess)
#
# if guess == answer:
#     print(f"Your guess is correct {answer} is correct")
# elif guess < answer:
#     print(f"the guess number {guess} is less than {answer} please try higher value")
#     guess = int(input())
#     if guess == answer:
#         print("Well done,You guess the right answer")
#     else:
#         print("Wrong try again!")
# elif guess > answer:
#     print(f"the guess number {guess} is greater than {answer} please try lower value")

########## Using conditions ###############
# answer = 5
# guess = int(input('Guess the number from 1 to 10 :'))
# print(guess)
#
# if guess == answer:
#     print('Your guess is correct')
#
# else:
#     if guess < answer:
#         print("Your guess is invalid Please guess greater number")
#     else:
#         print('Your guess is invalid Please guess lower number')
#     guess = int(input())
#     if guess == answer:
#         print("Well done guess is correct")
#     else:
#         print('Try again')


########## Simplified chained comparision ###################
age = int(input("How old are you ?"))
print(age)

# if age >= 16 and age <= 65:
# if 16 <= age >= 65:
#     print("Work hard")
# else:
#     print("Enjoy life")


# if 16 <= age >= 65:
#     print("Enjoy life")
# else:
#     print("work hard")


if age >16 or age <65:
    print('work hard')
else:
    print('enjoy')
