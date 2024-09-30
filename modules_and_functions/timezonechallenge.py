import pytz
import datetime

# for z in sorted(pytz.country_names):
#     print(f"The id {z} name is {pytz.country_names[z]} ",end=':')
#     if z in pytz.country_timezones:
#         print(pytz.country_timezones[z])
#     else:
#         print("No timezone is defined")
for number,(id,name) in enumerate(pytz.country_names.items()):
    print(number + 1,':',name)



lists = []
while len(lists) < 3:
    input_data = input("Enter the country name based on above data ").casefold()
    if input_data == 'stop':
        break
    country_code = None

    for code, name in pytz.country_names.items():
        if name.casefold() == input_data:
            utf_time = datetime.datetime.utcnow()
            timezone = pytz.timezone(pytz.country_timezones[code][0])
            current_time = datetime.datetime.now(timezone)
            print(f"The  country {name} with code '{code}' and the time {current_time} and time zone  {timezone} and utf time is {utf_time}")
            lists.append(input_data)
print(lists)

