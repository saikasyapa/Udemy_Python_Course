###### string concatination ###############
# print('Hello' + 'World')
# print('Hello' +' ' + 'World')
# a = 'Hello'
# b = 'Jannu'
# print(a+b)
# print(a + ' ' + b)


############## Escape Characters #########################
splitstring = "Hello my name is s.s.sai bhattar\niam from andhra pradesh\ncompleted graduation in 2019\nbut no use"
# print(splitstring)

# tabbedstring = "1\t2\t3\t4\t5\t6\t7\t8\t9\t10" #( \t means it gives 4 place spaces between elements)
# print(tabbedstring)

# print('the pet shop owner said"No,no,\'e\' uh,.....he\'s resting".')
# print("the pet shop owner said \"No ,no, 'e's uh,... he's resting\".")
# print("""the pet shop owner said "No, no,'e's uh,...he's resting".""")

# anothersplitstring = """Hello my name is s.s.sai bhattar
# iam from andhra pradesh
# completed graduation in 2019
# but no use
#
# """
#
# anothersplitstring1 = """Hello my name is s.s.sai bhattar\
# iam from andhra pradesh\
# completed graduation in 2019\
# but no use
#
# """
# print(anothersplitstring)
# print(anothersplitstring1)

# print("c:\Users\timbuchalka\notes.txt")   (### in this it giving error### )
# print("c:\\Users\\timbuchalka\\notes.txt")
# print(r"c:\Users\timbuchalka\notes.txt")

# name = "Hello World!"
# age = 55
# # print("my name is"+ name + "my age is" + age)
# print("my name is"+ name + "my age is", age)


############# operator Precedence #####################
# a = 12
# b = 3
# print(a+b / 3 - 4 * 12)   #op--35.0
# print(a+(b/3)-(4*12))
# print((((a+b)/3)-4)*12)

parrot = "Norwegian Blue"
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])

#
# indices = [3,4,9,3,6,8]
# # for index in indices:
# #     print(parrot[index])
#
# print('\n'.join(parrot[index] for index in indices))



############################ Negative indexing #########
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])

################## OR ##############

# print(parrot[3 - 14])
# print(parrot[4 - 14])
# print(parrot[9 - 14])
# print(parrot[3 - 14])
# print(parrot[6 - 14])
# print(parrot[8 - 14])

############### Slicing ################## start ,stop, step
# print(parrot[0:6]) ##Norweg
# print(parrot[3:5])
# print(parrot[0:5])
# print(parrot[:5])
# print(parrot[10:14])
# print(parrot[10:])
# print(parrot[0:6])
# print(parrot[6:])
# print(parrot[0:6] + parrot[6:])
# print(parrot[:])
# print(parrot[0:6])
# print(parrot[-4:-2])
# print(parrot[-4:12])


########### STep ##################
# print(parrot[0:6:1])  #Norweg
# print(parrot[0:6:2])   #Nre
# print(parrot[0::3])    # Nwi u
#
# number = "9,222,222,222,222,222,222"
# seperators = number[1::4]
# print(seperators)
#
# values = "".join(char if char not in seperators else " " for char in number).split()
# print([int(val) for val in values])

letters = "abcdefghijklmnopqrstuvwxyz"
back = letters[25::-1]
print(back)
print(letters[-10:-13:-1])
print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])
print(letters[:18:-1])
print(letters[25:22:-1])
print(letters[0])







