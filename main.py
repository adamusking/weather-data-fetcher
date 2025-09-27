import influxdb_client, time, requests, os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("INFLUX_TOKEN")
org = os.getenv("INFLUX_ORG")
url = os.getenv("INFLUX_URL")
bucket = os.getenv("INFLUX_BUCKET")

write_client = InfluxDBClient(url=url, token=token, org=org)
write_api = write_client.write_api(write_options=SYNCHRONOUS)

def get_weather_data():
    api_key = os.getenv("WEATHER_API_KEY")
    city_name = os.getenv("CITY") 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data, city_name
 
while True:
    data, city_name = get_weather_data()

    longitude = data['coord']['lon']
    latitude = data['coord']['lat']
    temperature = data['main']['temp'] - 273.15
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    country = data['sys']['country']
    weather = data['weather'][0]['main']


    point = (
        Point("weather_data")
        .tag("city", city_name)
        .field("city", city_name)
        .field("country", country)
        .field("description", weather)
        .field("latitude", latitude)
        .field("longitude", longitude)
        .field("temperature", temperature)
        .field("humidity", humidity)
        .field("pressure", pressure)
        .field("wind_speed", wind_speed)
    )
    write_api.write(bucket=bucket, org=org, record=point)
    print("Data written successfully!")
    time.sleep(60) 
