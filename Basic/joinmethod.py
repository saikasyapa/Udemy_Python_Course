# menu = [
#     ["eggs", "bacon"],
#     ["eggs","sausage", "bacon"],
#     ["eggs", "spam"],
#     ["eggs", "bacon", "spam"],
#     ["eggs", "bacon", "sausage", "spam"],
#     ["spam", "bacon", "sausage", "spam"],
#     ["spam", "bacon","spam", "spam", "bacon", "spam"],
#     ["spam", "sausage", "spam", "spam", "bacon", "spam","tomato", "spam"],
# ]
#
# for meal in menu:
#     for index in range(len(meal) - 1,-1,-1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(", ".join(meal))

flowers = [
    "Daffodil","Jasmine","lille","rose","mandaram"
]
# for flower in flowers:
#     print(flower)

seperator = " | "
output = seperator.join(flowers)
print(output)

seperator1 = " $$ "
output1 = seperator1.join(flowers)
print(output1)

print(" %%% ".join(flowers))


