# numbers = {*""}
## another way
# numbers = {*{}}
# numbers = set()
# print(type(numbers))
#
# numbers.add(1)
# print(numbers)
#
# for i in range(1,20):
#     numbers.add(i)
# print(numbers)
#
# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value to add :- "))
#     numbers.add(next_value)
# print(numbers)

###output #####
# Please enter your next value to add :- 55
# Please enter your next value to add :- 55
# Please enter your next value to add :- 55
# Please enter your next value to add :- 55
# Please enter your next value to add :- 66
# Please enter your next value to add :- 66
# Please enter your next value to add :- 77
# {1, 66, 77, 55}


data = ['blue','red','blue','brown','pink','red','silver','pink']
# create a data from a list, to remove dupicates
unique_data = sorted(set(data))
print(unique_data)
#create a list of unique colours, keeping the order they appered
unique_data = list(dict.fromkeys(data))
print(unique_data)