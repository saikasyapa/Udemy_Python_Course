# animals = {
#     "lion" : "scary",
#     "elephant" : "big",
#     "teddy" : "cuddly"
# }
# things = animals.copy()
# animals["teddy"] = "toy"
# print(things["teddy"])
# print(animals)

lion_list = ["scary","big","cat"]
elephant_list = ["big","grey","wrinkled"]
teddy_list = ["cuddly","stuffed"]
animals = {
    "lion" : lion_list,
    "elephant" :elephant_list,
    "teddy" : teddy_list
}
# things = animals.copy()
#
# print(things["teddy"])
# print(animals["teddy"])
#
# print()
# things["teddy"].append("toy")
# print(things["teddy"])
# print(animals["teddy"])
########################### in this they use same list for animals and things also because of that if you add any thing to one dict it is applied to all
######### Deep Copy ##############
import copy

# lion_list = ["scary","big","cat"]
# elephant_list = ["big","grey","wrinkled"]
# teddy_list = ["cuddly","stuffed"]
# animals = {
#     "lion" : lion_list,
#     "elephant" :elephant_list,
#     "teddy" : teddy_list
# }
### for shallow copy
# things = animals.copy()
#
# ### for deep copy
# things = copy.deepcopy(animals)
#
# print(id(things["teddy"]),things["teddy"])
# print(id(animals["teddy"]),animals["teddy"])
#
# print()
# things["teddy"].append("toy")
# print(things["teddy"])
# print(animals["teddy"])
