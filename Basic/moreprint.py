name = "Tim"
age = "100"
print(name, age,"Python", 2020)
print(name, age,"Python", 2020, sep = ", ")


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

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item , end=", ")       ######### added end=" "
    print()