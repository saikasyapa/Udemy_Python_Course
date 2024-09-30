data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]


# plants_filename = "flowers_print.txt"
#
# with open(plants_filename,'w') as plants:
#     for plant in data:
#         print(plant,file=plants)
#
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.strip())
# print(new_list)

#### because of __str__ method in print it is printing every line in new line

plants_filename = "flowers_write.txt"

with open(plants_filename,'w') as plants:
    for plant in data:
        plants.write(plant)

number_file = "number_print.txt"
with open(number_file,'w') as file:
    for number in range(12):
        print(number,file=file)

# number_file = "number_print_write.txt"
# with open(number_file,'w') as file:
#     for number in range(12):
#         file.write(number)

# Traceback (most recent call last):
#   File "D:\Tim Buchalka\pythonProject\read_write\save_flowers.py", line 52, in <module>
#     file.write(number)
# TypeError: write() argument must be str, not int

number_file = "number_print_write.txt"
with open(number_file,'w') as file:
    for number in range(12):
        file.write(str(number) + '\n')