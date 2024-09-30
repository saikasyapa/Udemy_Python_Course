
small_ints = set(range(20))
print(small_ints)

# small_ints.clear()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)
## Ensure that when we're done,something no longer exists. in this case , we don't care if it wes alredy there or not-we just it gone
small_ints.discard(99)
print(small_ints)
## remove something if it exists, but provide some sort of notification if it doesn,t
small_ints.remove(98)
print(small_ints)
# Traceback (most recent call last):
#   File "D:\Tim Buchalka\pythonProject\sets\removeitems.py", line 13, in <module>
#     small_ints.remove(98)
# KeyError: 98
