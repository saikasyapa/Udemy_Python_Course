############## String Operators ####################

# string1 = "Hi"
# string2 = " hello"
# string3 = " namaste"
# string4 = " vanakam"
# print(string1 + string2 + string3 + string4)
# print("Hi" " hello" " namaste" " vanakam")
#
# print("hello " * 5)
# # print("hello" * 6 +5)
# print("hello " * (6 +5))
# print("hello " * 6 +'5')
#
# today = "friday"
# print("day" in today)
# print('fri' in today)
# print('rid' in today)
# print('aaa' in today)
# print('bbb' in today)


################## String Replacement Fields ##################
######### . format method ###

# age = 26
# print("Iam " + str(age) + " years old")
# print("Iam {0} years old".format(age))
#
# print("there are {0} days in {1},{2},{3},{4},{5},{6} and {7} months"
#       .format(31,'jan','mar','may','jul','aug','oct','dec'))
#
# print("jan:{2}, \nfeb:{0}, \nmar:{2}, \napr:{1}, \nmay:{2}, \njun:{1}, \njul:{2}, \naug:{2}, \nsep:{1}, \noct:{2}, \nnov:{1}, \ndec:{2}"
#       .format(28 or 29,30,31))

######## string format #############
# for i in range(1, 13):
#     # print("the count of {0} square are {1} and cube are {2}".format(i,i ** 2,i **3))
#     # print("the count of {0:2} square are {1:4} and cube are {2:4}".format(i, i ** 2, i ** 3))
#     ################# For Left Alligned ###############
#     # print("the count of {0:2} square are {1:<3} and cube are {2:<4}".format(i, i ** 2, i ** 3))
#     ################# For Center ###############
#     print("the count of {0:2} square are {1:^3} and cube are {2:^4}".format(i, i ** 2, i ** 3))
#       print("the count of {:2} square are {:^3} and cube are {:^4}".format(i, i ** 2, i ** 3)) but you want to use format multiple times you need to enter values


# print(" Pi is approximately {0:5}".format(22/7))
# print(" Pi is approximately {0}".format(22/7))
# print(" Pi is approximately {0:12}".format(22/7))
# print(" Pi is approximately {0:12f}".format(22/7))
# print(" Pi is approximately {0:12.50f}".format(22/7))
# print(" Pi is approximately {0:62.50f}".format(22/7))
# print(" Pi is approximately {0:72.50f}".format(22/7))

##################### F-Strings ########################
# age=24
# print(age)
# age_in_w = "2 years"
# name ="sai"
# print(name +f"is {age} years old")
#
# print(f" Pi is approximately {22/7} ")

################### This is python 2 Interpolation concept ###############
age = 24
print("my age is %d years" % age)
major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age,major,6,minor))


