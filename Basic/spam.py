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

for item in menu:
    if 'spam' not in item:
        print(item)

        for meal in item:
            print(meal)
    # find "spam" count in the list
    else:
        print(f"the total spam count in the lists are {item} is {item.count('spam')}")

