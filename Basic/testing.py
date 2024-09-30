

data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
# data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191]
# data = [104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
# data = [104,105,110,120,130,130,150,160,170,183,185,187,188,191]
# data = [1040,1050,1100,1200,1300,1300,1500,1600,1700,1830,1850,1870,1880,1910]
# data = []
print(data)
min_valid = 100
max_valid = 200
# #  process the low values in the list
# stop = 0
# for number, value in enumerate(data):
#     if value >= min_valid:
#         stop = number
#         break
# print(stop)
# del data[:stop]
# print(data)
#
# # Process the high values in the list
# #
# start = 0
# for index in range(len(data)-1,-1,-1):
#     if data[index] <= max_valid:
#         start = index + 1
#         break
# print(start)
# del data[start:]
# print(data)


##### another method ###########
# for index in range(len(data)-1,-1,-1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index,data)
#         del data[index]
# print(data)

##### another method - 1 ###########

top_index = len(data) - 1
for number,value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - number,value)
        del data[top_index - number]
print(data)
