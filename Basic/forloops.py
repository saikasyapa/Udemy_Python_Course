# parrot = 'Norweigen Blue'
#
# for i in range(len(parrot)):
#
#     print('*' * i)

# numbers = "9,223;372:036 854,775;807"
# seperators = " "   ##(empty string)
# values = " "
# for char in numbers:
#     if not char.isnumeric():
#         seperators = seperators + char
#     elif char.isnumeric():
#         values = values + char
# print(values)
# print(seperators)





# number = ''           ##(empty string)
# for nume in numbers:
#     if nume.isnumeric():
#         number = number + nume
# print(number)




# import re
# numbers = "9,223;372:036 854,775;807"
# seperators = " "
# values = []
#
# for char in numbers:
#     if not char.isnumeric():
#         seperators = seperators + char
# split_values = re.split(r'[^0-9]+', numbers)
# for value in split_values:
#     if value:
#         values.append(int(value))
# print("values",values)
# print("seperators",seperators)

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# # Use a for loop and an if statement to print just the capitals in the quote above.
# for i in quote:
#     if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         print(i)

# for char in quote:
#     if char.isupper():
#         print(char)



###################### range ##############################
# for i in range(1,20):
#     print(f"the num is {i}")
#
# ##### steps ###
# for i in range(0,20,2):
#     print(f"the num is {i}")
#
# for i in range(20,0,-2):
#     print(f"the num is {i}")

# age = int(input("Enter your age :"))
# if age in range(18,66):
#
#     print("Do your work")
# else:
#     print('Enjoy your life')


# for i in range(0,101):
#     z = i%7
#     if z==0:
#         print(i)


################# Nested for loop ###############

# for i in range(1,13):
#     for j in range(1,13):
#         print(f"{i}\t times of {j}\t is {i * j}\t")
#     print(50 * '*')


############### Continue #############

# shooping_list = ['Rice','Veges','Spices','snacks','milk']
# for i in shooping_list:
#     if i != 'snacks':
#         print(i)

# shooping_list = ['Rice','Veges','Spices','snacks','milk']
# for i in shooping_list:
#     if i == 'snacks':
#         continue
#     print(i)

shooping_list = ['Rice','Veges','Spices','snacks','milk','milk1','milk2']
# item_to_find = "snacks"
# found_at = None
# for index in range(len(shooping_list)):
#     if shooping_list[index] == item_to_find:
#         found_at = index
#
# print(found_at)
# shooping_list = ['Rice','Veges','Spices','snacks','milk','milk1','milk2']
# item_to_find = "snacks"
#
# for index in range(len(shooping_list)):
#     if shooping_list[index] == item_to_find:
#         print(shooping_list[index],index)
#         break
# else:
#     print('item not found')

########## simple Way #################

shooping_list = ['Rice','Veges','Spices','snacks','milk','milk1','milk2']

if 'snacks' in shooping_list:
    print(" The Position of snacks item is",shooping_list.index('snacks'))









