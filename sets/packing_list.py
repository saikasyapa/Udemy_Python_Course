travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}
#
# print("Please choose your mode of travel:")
# for key, value in travel_mode.items():
#     print(f"{key}: {value}")
#     # Python 3.5 and earlier
#     # print("{}: {}".format(key, value))
#
# mode = "-"
# while mode not in travel_mode:
#     mode = input("> ")
#
# if mode == "2":
#     # for restricted_item in restricted_items:
#     #     items.discard(restricted_item)
# ############ remove
#     for restricted_item in restricted_items:
#         items.remove(restricted_item)
#
# # Traceback (most recent call last):
# #   File "D:\Tim Buchalka\pythonProject\sets\packing_list.py", line 53, in <module>
# #     items.remove(restricted_item)
# # KeyError: 'catapult'
#
#
# # print the packing list
# print("You need to pack:")
# for item in sorted(items):
#     print(item)
