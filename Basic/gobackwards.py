# # data  = [101,105,109,111,152,4,168,19,199,178,3,2,145,182]
#
# min_value = 100
# max_value = 200
#
# for index in range(len(data) - 1,-1,-1):
#     if data[index] < min_value or data[index] > max_value:
#         print(index,data)
#         del data[index]
# print(data)

data  = [101,105,109,111,152,4,168,19,199,178,3,2,145,182]
min_value = 100
max_value = 200
top_index = len(data) - 1
for number,value in enumerate(reversed(data)):
    if value < min_value or value > max_value:
        print(top_index - number,value)
        del data[top_index - number]
print(data)