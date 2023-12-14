import requests
def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    weather_description = data['weather'][0]['description']
    temp_kelvin = data['main']['temp']

    temp_celsius = temp_kelvin - 273.15

    return weather_description, temp_celsius

def main():
    api_key = "8197212976a1124ab80f5bab0087f414"
    city_name = input("Enter the name of a municipality: ")
    weather_description, temp_celsius = get_weather(api_key, city_name)

    print(f"Weather in {city_name}: {weather_description}")
    print(f"Temperature: {temp_celsius:.2f}°C")

if __name__ == "__main__":
    main()