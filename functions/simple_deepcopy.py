# from contents import recipes
# def my_deepcopy(d):
#     new_dict = {}
#     for key,value in d.items():
#         new_value = value.copy()
#         new_dict[key] = new_value
#
#
#     return new_dict
#
#
# recipes_copy = my_deepcopy(recipes)
# recipes_copy["Butter chicken"]["ginger"] = 300
# print(recipes_copy["Butter chicken"]["ginger"])
# print(recipes["Butter chicken"]["ginger"])


############# storing in list
# from shall_copy import animals
# def my_deepcopy(d):
#     new_dict = []
#     for key,value in d.items():
#         new_dict.append((key,value.copy()))
#     return new_dict
#
#
# animals_copy = my_deepcopy(animals)
# for i,(key,value) in enumerate(animals_copy):
#     if key == "lion":
#         value.append("cruel")
# print(animals_copy['lion'])
# print(animals['lion'])

############## storing in dict
# from shall_copy import animals
def my_deepcopy(d):
    new_dict = {}
    for key,value in d.items():
        new_dict[key] = value.copy()
    return new_dict
#
# animals_copy = my_deepcopy(animals)
# animals_copy["lion"].append("cruel")
# print(animals_copy["lion"])
# print(animals['lion'])
import copy
original = {
    "Tim" : ["Buchalk", ["Programmer", "Teacher"]],
    "j-k" : ["Roberts",["Programmer", "Teacher"]]

}
copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["Tim"].append("Australia")
original["j-k"].append("U.K")
original["Tim"][1].append("Cashier")
original["j-k"][1].append("Mechanic")
print(original)
print(copy_1)
print(copy_2)