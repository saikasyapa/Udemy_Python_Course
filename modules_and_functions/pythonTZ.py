import pytz
import datetime
from datetime import time
country = "Asia/Kolkata"

dis = pytz.timezone(country)
local_time = datetime.datetime.now(tz= dis)
# print(f"The datetime in {country} is {local_time}")
# print(f"UTC time is {datetime.datetime.utcnow()}")

# for x in pytz.all_timezones:
#     print(x)

# for y in sorted(pytz.country_names):
#     print(y +":"+pytz.country_names[y])

# for z in sorted(pytz.country_names):
#     print(f"The country : {z} name is {pytz.country_names[z]} and the timezone is {pytz.country_timezones.get(z)}")

###################### OR #####################################

for z in sorted(pytz.country_names):
    print(f"The id {z} name is {pytz.country_names[z]} ",end=':')
    if z in pytz.country_timezones:
        print(pytz.country_timezones[z])
    else:
        print("No timezone is defined")


############################### Adding time to the above used data ################################

# for z in sorted(pytz.country_names):
#     print(f"The id {z} name is {pytz.country_names[z]} ",end=':')
#     if z in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[z]):
#             tz_to_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz = tz_to_display)
#             print(zone,local_time)
#     else:
#         print("No timezone is defined ")