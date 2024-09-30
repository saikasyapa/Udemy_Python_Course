import json
import urllib.request
# json_data_source = 'data.json'
#
# with open(json_data_source,encoding='utf-8') as data:
#     item = json.load(data)
# print(item['description'])
# for year,value in item['data'].items():
#     year, value = int(year), float(value)
#     print(f"{year}\t{value}")

json_path = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/tavg/land_ocean/1/8/1880-2024/data.json'

with urllib.request.urlopen(json_path) as json_stream:
    data= json_stream.read().decode('utf-8')
    item = json.loads(data)                            #### changed load to loads
print(item)

for year,value in item['data'].items():
    year, value = int(year), float(value)
    print(f"{year}\t{value}")