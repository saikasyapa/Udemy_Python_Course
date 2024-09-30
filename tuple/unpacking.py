# x,y,z = 12,16,14
# print(x)
# print(y)
# print(z)
#
# #### Unpacking Tuple
# data = 1,2,3
# x,y,z = data
# print(x)
# print(y)
# print(z)
#
# data = [12,13,14]
# p,q,r = data
# print(p)
# print(q)
# print(r)

# for number,items in enumerate("abcdefg"):
#     print(number,items)

for items in enumerate("abcdefg"):
    print(items)
#### Unpacking Tuples
for items in enumerate("abcdefg"):
    number, value = items
    print(number,value)

