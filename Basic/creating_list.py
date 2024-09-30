# even = [2,4,6,8]
# odd = [1,3,5,7,9]
# print(even + odd)
# sorted_list = sorted(even + odd)
# print(sorted_list)
# all_elements = even+odd
# all_elements.sort()
# print(all_elements)
# digits = sorted("5648513247")
# print(digits)
# digits1 = list("5648513247")
# print(digits1)
# sorted_digits1 = sorted(digits1)
# print(sorted_digits1)
# print(sorted_list is all_elements)
# print(sorted_list == all_elements)

even = [2,4,6,8]
odd = [1,3,5,7,9]
numbers = even +odd
print(numbers)

more_numbers = list(numbers)   ##old
more_numbers = numbers[:]      ## uses in python 2
more_numbers = numbers.copy()  ###Imp uses in python 3
print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)