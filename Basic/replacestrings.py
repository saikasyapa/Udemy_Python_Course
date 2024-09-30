# computer_parts = ["computer","Monitor","Keyboard","Mouse","Mouse pad"]
# print(computer_parts)
#
# print(computer_parts[2:])
# computer_parts[2:] = ['Trackball']
# print(computer_parts)

# data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
# print(data)
# del data[0:2]
# print(data)

# del data[-2:]
# print(data)

# min_valid = 100
# mav_valid = 200

# for number, value in enumerate(data):
#     if (value < min_valid) or (value>mav_valid):
#         del data[number]
# print(data)
data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
print(data)
min_valid = 100
max_valid = 200
# #  process the low values in the list
stop = 0
for number, value in enumerate(data):
    if value >= min_valid:
        stop = number
        break
print(stop)
del data[:stop]
print(data)

# Process the high values in the list
#
start = 0
for index in range(len(data)-1,-1,-1):
    if data[index] <= max_valid:
        start = index + 1
        break
print(start)
del data[start:]
print(data)


