input_filename = "country_info.txt"
countries = {}
with open(input_filename) as country_file:
    country_file.readline()

    for row in country_file:
        data  = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep = '\n\t')
        country_dict = {'country' : country,
                        'capital' : capital,
                        'code' : code,
                        'code3' : code3,
                        'dialing' : dialing,
                        'timezone' : timezone,
                        'currency' : currency
                        }
        # country_dict = dict(
        #     country = country,
        #     capital = capital,
        #     code = code,
        #     code3 = code3,
        #     dialing = dialing,
        #     timezone = timezone,
        #     currency = currency

        # )
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # countries[code.casefold()] = country_dict
print(countries)
# choice = input("Enter the country name to find city").casefold()
# if choice in countries:
#     country_data = countries[choice]
#     print(country_data['capital'])
# elif choice == 'quit':
#     print("end")






