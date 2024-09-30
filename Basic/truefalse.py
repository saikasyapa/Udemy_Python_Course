# day = 'monday'
# temp = 30
# raining = True
# if day == 'monday' and temp > 27 or not raining:
#     print('Go swimming')
# else:
#     print('Keep Quiet and learn python')
#
#
# day = 'monday'
# temp = 30
# raining = True
# if (day == 'monday' and temp > 27) or raining:   #### in this it will execute and first and next or
#     print('Go swimming')
# else:
#     print('Keep Quiet and learn python')


###################### Truthy Values ####################

# name = input("Please enter your name")
# if name:
#     print(f"Hello {name}")
# else:
#     print("Hello no name")

name = input("Please enter your name")
if name != " ":
    print(f"Hello {name}")
else:
    print("Hello no name")