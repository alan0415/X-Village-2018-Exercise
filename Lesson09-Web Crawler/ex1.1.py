import requests
import json

url = 'https://www.metaweather.com/api/location/2306179/2018/7/18'
r = requests.get(url)
r.encoding = 'utf-8' 
data = json.loads(r.text)
list1 = data[0]
print(list1['weather_state_name'])