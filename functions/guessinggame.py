# # # # def guess(number):
# # # #     if (number >=16) and (number<=65):
# # # #         return "Work Hard"
# # # #     else:
# # # #         return "Enjoy"
# # # #
# # # # print(guess(25))
# # # # print(guess(5))
# # #
# # #
# # #
# # # # def guess():
# # # #     number = int(input("Enter your guess"))
# # # #     if (number >=16) and (number<=65):
# # # #         return "Work Hard"
# # # #     else:
# # # #         return "Enjoy"
# # # #
# # # # print(guess())
# # # # import random
# # # #
# # # #
# # # #
# # # #
# # # # def guess():
# # # #
# # # #     while True:
# # # #         answer = random.randint(1, 10)
# # # #         number = int(input("Enter your guess"))
# # # #         if number == answer:
# # # #             print("Well Done")
# # # #             break
# # # #         if number < answer:
# # # #             print("try higher value")
# # # #             number = int(input())
# # # #             if number == answer:
# # # #                 print("Well done!!!")
# # # #             else:
# # # #                 print("Try next time")
# # # #         elif number > answer:
# # # #             print("try Lower value")
# # # #             number = int(input())
# # # #             if number == answer:
# # # #                 print("Well done!!!")
# # # #             else:
# # # #                 print("Try next time")
# # # # guess()
# # #
# # # def guess():
# # #     low = 1
# # #     high = 1000
# # #
# # #     print(f"Please think of the number between {low} and {high}")
# # #     input("Press Enter to start")
# # #
# # #     guesses = 1
# # #     while True:
# # #         print(f"Calculating range is {low} to {high} ")
# # #         guess1 = low + (high - low) // 2
# # #         high_low = (input(f"my guess is {guess1}.Should i guess higher or lower? "
# # #                           "Enter h or l, or c if my guess is correct").casefold())
# # #
# # #         if high_low == "h":
# # #             low = guess1 + 1
# # #
# # #         elif high_low == "l":
# # #             high = guess1 - 1
# # #
# # #         elif high_low == "c":
# # #             print(f"I got guessing number  {guess1} in {guesses} guesses")
# # #             break
# # #         else:
# # #             print("Please enter h,l or c")
# # #
# # #         guesses = guesses + 1
# # #
# # # guess()
# #
# # # def sum_eo(n,t):
# # #     total = 0
# # #     if t =="e":
# # #         for i in range(1,n+1):
# # #             if i % 2 ==0:
# # #                 total = total + i
# # #
# # #     elif t=='o':
# # #         for i in range(1,n+1):
# # #             if i %2 != 0:
# # #                 total = total + i
# # #     else:
# # #         return  -1
# # #     return total
# # # print(sum_eo(15,'o'))
# #
# # import random
# # def get_integer(prompt):
# #     """
# #     Get an integer from Standard Input(stdin).
# #
# #     the user, until a valid `int` is entered.
# #
# #     :param prompt:The String that the user will see, when
# #      they're prompted to enter the value.
# #
# #     :return:The integer that the user enters.
# #     """
# #     while True:
# #         temp = int(input(prompt))
# #         # if not temp.is_integer():
# #         #     print("Enter integer values only")
# #         if temp.isnumeric():
# #             return int(temp)
# #         else:
# #             print(f"{temp} is invalid format")
# # highest = 1000
# # answer = random.randint(1,highest)
# # print(answer)
# # guess = 0
# # print("Please guess number between 1 to 1000")
# # while guess != answer:
# #     guess = get_integer(": ")
# #
# #     if guess == 0:
# #         break
# #     if guess == answer:
# #         print("Well done!, You guess correct number")
# #         break
# #     else:
# #         if guess < answer:
# #             print("Guess higher number")
# #         else:
# #             print("Guess Lower number")
# #
# #
# #
# #
# # def fizz_buzz(choice):
# #     # try:
# #     #     choice = int(input("Enter your number"))
# #     # except ValueError:
# #     #     return "Error: Please enter valid integer value."
# #
# #     if (choice % 3 == 0) and (choice % 5 == 0):
# #         return "fizz buzz"
# #     elif choice % 3 == 0:
# #         return "fizz"
# #     elif choice % 5 == 0:
# #         return "buzz"
# #
# #     else:
# #         return choice
#
#
# def fizz_buzz(choice):
#     # try:
#     #     choice = int(input("Enter your number"))
#     # except ValueError:
#     #     return "Error: Please enter valid integer value."
#
#     if (choice % 3 == 0) and (choice % 5 == 0):
#         return "fizz buzz"
#     elif choice % 3 == 0:
#         return "fizz"
#     elif choice % 5 == 0:
#         return "buzz"
#
#     else:
#         return choice
#
#
# input("Press Enter to start")
# print()
#
# next_number = 0
# while next_number<99:
#     next_number = next_number + 1
#     print(fizz_buzz(next_number))
#     next_number = next_number +1
#     correct_answer = fizz_buzz(next_number)
#
#     player_answer = input("you go")
#     if player_answer !=correct_answer:
#         print("You lose")
#         break
#     else:
#         print("well done")

def factorial(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must not non-negative number")
    result = 1
    for i in range(1, number +1):
        result = i * result
        print(f"{i} {result}")
    return result

print(factorial(36))
