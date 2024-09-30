

#
# available_parts = {
#     "1" : "computer",
#     "2" : "moniter",
#     "3" : "keyboard",
#     "4" : "mouse",
#     "5" : "printer"
# }
# for n,i in enumerate(available_parts):
#     print(n + 1,available_parts[i])
# # valid_choices = []
# # for i in range(1,len(available_parts) + 1):
# #     valid_choices.append(str(i))
#
# computer_parts = []
# current_choice = None
# while True:
#     current_choice = input("Enter the value")
#     if current_choice == '0':
#         print("iam done")
#         break
#     if current_choice in available_parts:
#         choosen_part = available_parts[current_choice]
#         computer_parts.append(choosen_part)
#         print(f"You are selected {choosen_part} and the list is {computer_parts}")
#     else:
#         print("Enter valid number")

################# Code from the video #################
# available_parts = {
#     "1" : "computer",
#     "2" : "moniter",
#     "3" : "keyboard",
#     "4" : "mouse",
#     "5" : "printer"
# }
# current_choice = None
# choices = []
#
# while current_choice != "0":
#     if current_choice in available_parts:
#         chosen_part = available_parts[current_choice]
#         if chosen_part in choices:
#             print(f"removing {chosen_part}")
#             choices.remove(chosen_part)
#         else:
#
#             print(f"adding{chosen_part}")
#             choices.append(chosen_part)
#         print(f"Your list now contains {choices}")
#     else:
#         print("Please add options from the list")
#         for key,value in available_parts.items():
#             print(f"{key} : {value}")
#
#
#         print("0: to finish")
#     current_choice = input("Enter your value >")



available_parts = {
    "1" : "computer",
    "2" : "moniter",
    "3" : "keyboard",
    "4" : "mouse",
    "5" : "printer"
}
current_choice = None
choices = {}

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in choices:
            print(f"removing {chosen_part}")
            choices.pop(current_choice)
        else:

            print(f"adding{chosen_part}")
            choices[current_choice] = chosen_part
        print(f"Your list now contains {choices}")
    else:
        print("Please add options from the list")
        for key,value in available_parts.items():
            print(f"{key} : {value}")


        print("0: to finish")
    current_choice = input("Enter your value >")


