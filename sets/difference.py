# from primes_squares import squares_generator,primes_generator
#
# evens =set(range(0,50,2))
# odds = set(range(1,50,2))
#
# primes = set(primes_generator(100))
# print(f"primes {primes}")
# squares = set(squares_generator(100))
# print(f"squares {squares}")
#
# print(odds.difference(primes))
# print(odds - primes)
# print(primes - odds)
# from packing_list import *
# print("Please choose option : ")
# for key, value in travel_mode.items():
#     print(f"{key} : {value}")
#
# mode  = ""
# while mode not in travel_mode:
#     mode = input('>')
#
# if mode =="2":
#     items =items - restricted_items
#            ## or
#     items.difference_update(restricted_items)
#
#
#
# print("You need to pack")
# for item in sorted(items):
#     print(item)

favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

basket = {'garlic crusher',
          'stirling engine',
          'frying pan',
          'shirt',
          'bush hat',
          }

# Add your code here.
suggestions=favourites-basket
print(sorted(suggestions))
