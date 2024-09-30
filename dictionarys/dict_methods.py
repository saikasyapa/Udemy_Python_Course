d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv":'four'
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# v =d.values()
# print(v)
# d[10]= "Ten"
# print(d)

#####dict.fromkeys
# new_dict = dict.fromkeys(pantry_items,0)
# print(new_dict)

### keys
# keys = d.keys()
# print(keys)
#
# for item in d.keys():
#     print(item)

########### update
# d2 = {
#     7 : "lucky seven",
#     10 : "ten",
#     3 : "this is three"
# }
# d.update(d2)
# for key, value in d.items():
#     print(key,value)
# print(90 * "*")
# d.update(enumerate(pantry_items))
# for i,j in d.items():
#     print(i,j)

############## finding key based on value
keys = list(d.keys())
values = list(d.values())
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {[key]}")

for key,value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key {[key]}")
