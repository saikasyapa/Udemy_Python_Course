# from contents import pantry,recipes
#
#
#
# # def add_shopping_item(data,item,amount):
# #     data.append((item,amount))
# #
# # display_dict = {}
# # for index,key in enumerate(recipes):
# #     display_dict[str(index + 1)] = key
# #
# # # for index,key in enumerate(recipes):
# # #     recipe_number = str(index + 1)
# # #     display_dict[recipe_number] = key
# #
# # shopping_list = []
# # while True:
# #     print("Please choose your recipe")
# #     print(80 * "*")
# #     for key,value in display_dict.items():
# #         print(f"{key} - {value}")
# #
# #     choice = input("Select your choice :-")
# #     if choice == '0':
# #         print("Iam done! , I dont want anything")
# #         break
# #     elif choice in display_dict:
# #         selected_item = display_dict[choice]
# #         print(f"You selected items {selected_item}")
# #         print("Checking Ingredients....")
# #         ingredients = recipes[selected_item]
# #         print(ingredients)
# #         for food_item, required_quantity in ingredients.items():
# #             quantity_in_pantry = pantry.get(food_item, 0)
# #             if required_quantity <= quantity_in_pantry:
# #                 print(f"\t{food_item} OK")
# #             else:
# #                 quantity_to_buy = required_quantity - quantity_in_pantry
# #                 print(f"\tyou need to buy {quantity_to_buy} of {food_item}")
# #                 add_shopping_item(shopping_list,food_item,quantity_to_buy)
# # for j in sorted(shopping_list):
# #     print(j)
#
#
# def add_shopping_item(data,item,amount):
#     if item in data:
#         data[item] += amount
#     else:
#         data[item] = amount
#
# display_dict = {}
# for index,key in enumerate(recipes):
#     display_dict[str(index + 1)] = key
#
# # for index,key in enumerate(recipes):
# #     recipe_number = str(index + 1)
# #     display_dict[recipe_number] = key
#
# shopping_list = {}
# while True:
#     print("Please choose your recipe")
#     print(80 * "*")
#     for key,value in display_dict.items():
#         print(f"{key} - {value}")
#
#     choice = input("Select your choice :-")
#     if choice == '0':
#         print("Iam done! , I dont want anything")
#         break
#     elif choice in display_dict:
#         selected_item = display_dict[choice]
#         print(f"You selected items {selected_item}")
#         print("Checking Ingredients....")
#         ingredients = recipes[selected_item]
#         print(ingredients)
#         for food_item, required_quantity in ingredients.items():
#             quantity_in_pantry = pantry.get(food_item, 0)
#             if required_quantity <= quantity_in_pantry:
#                 print(f"\t{food_item} OK")
#             else:
#                 quantity_to_buy = required_quantity - quantity_in_pantry
#                 print(f"\tyou need to buy {quantity_to_buy} of {food_item}")
#                 add_shopping_item(shopping_list,food_item,quantity_to_buy)
# for j in shopping_list.items():
#     print(j)

# # We need an empty dictionary, to store and display the letter frequencies.
# word_count = {}
#
# # Text string
# text = "Later in the course, you'll see how to use the collections Counter class."
#
# # Your code goes here ...
# for char in text.casefold():
#     if char.isalnum():
#         if char in word_count:
#             word_count[char] = word_count[char] + 1
#         else:
#             word_count[char] = 1
#
# # Printing the dictionary
# for letter, count in sorted(word_count.items()):
#     print(letter, count)


