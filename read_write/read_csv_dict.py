import csv

cerial_filename = "cereal_grains.csv"

with open(cerial_filename,encoding='utf-8',newline='') as cerials_file:
    reader = csv.DictReader(cerials_file)
    for row in reader:
        print(row)