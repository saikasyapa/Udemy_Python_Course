import csv

csv_file = "cereal_grains.csv"

with open(csv_file,encoding='utf-8',newline="") as csv_filee:
    reader =csv.reader(csv_filee,quoting=csv.QUOTE_NONNUMERIC)     ## TO USE 'quoting=csv.QUOTE_NONNUMERIC' THIS ALL THE STRING ARE QUATED AND NUMBERS PRINTED AS FLOATS
    for row in reader:
        print(row)

