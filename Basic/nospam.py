from os import remove

menu = [
    ["eggs", "bacon"],
    ["eggs","sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs", "bacon", "spam"],
    ["eggs", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "bacon","spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "spam", "bacon", "spam","tomato", "spam"],
]
# for meal in menu:
#     for number, item in enumerate(meal):
#         if meal[number] == "spam":
#             del meal[number]
#     print(meal)

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item)
#     print()

# for meal in menu:
#     filtered_meal = [item for item in meal if item != "spam"]
#     print(filtered_meal)

for meal in menu:
    for index in range(len(meal) - 1,-1,-1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)









