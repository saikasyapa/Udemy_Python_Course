import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print(f"native local time {local_time} ")
print(f"native UTF time {utc_time}")

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)
print(f"Aware local time {aware_local_time}, time zone is {aware_local_time.tzinfo} ")
print(f"Aware UTC {aware_utc_time} , time zone {aware_utc_time.tzinfo}")

gap_time = datetime.datetime(2015, 10 ,25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())     #1445716800.0

s = 1445733000
t =s + (60 * 60)
gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print(f"{s} seconds since the epoch is {dt1}")
print(f"{t} seconds since the epoch is {dt2}")

