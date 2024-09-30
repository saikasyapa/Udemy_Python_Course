import csv
input_filename = "country_info.txt"
countries = {}
with open(input_filename, encoding='utf-8',newline='') as country_file:
    reader= csv.DictReader(country_file, delimiter='|')
    for row in reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row

while True:
    choosen_country = input("Please enter the name odf the country:")
    country_key = choosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {choosen_country} is {country_data['Capital']}")
    elif choosen_country == 'quit':
        break










