# pangram = "The quick brown fox jumps over a lazy dog"
# pangram1 = """The quick brown
# fox jumps\tover
# a lazy dog"""
# words = pangram.split()
# print(words)
# words1 = pangram1.split()
# print(words1)
#
# numers = "1,333,444,555,666,7,88,999,666,55,6666"
# numb = numers.split(",")
# print(numb)
from os.path import split

from gobackwards import value, number

# genetrted_list = ['9',' ',
#                     '2','2','3',' ',
#                     '3','7','7',' ',
#                     '0','3','6',' ',
#                     '8','5','4',' ',
#                     '7','7','5',' ',
#                     '8','0','7']
# values = "".join(genetrted_list)
# print(values)
# values_list = values.split()
# print(values_list)
#
# for number,items in enumerate(values_list):
#     print(items)
#
# for index in range(len(values_list)):
#     values_list[index] = int(values_list[index])
# print(values_list)
#
#
# ########### 2nd method to print only numbers########
#
# integer_values = []
# for value in values_list:
#     integer_values.append(value)
# print(integer_values)

inputs = input("Enter the values of a,b,c and separate them using comma's")
inputs1 = inputs.split(",")
numbers = []
for num in inputs1:
    numbers.append(int(num))
a, b, c = numbers
result = a+b-c
print(result)