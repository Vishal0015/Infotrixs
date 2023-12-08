import requests
import json
import time

API_KEY = 'cb4f53c1eb9193589b4cf83b62f901a1'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

favorite_cities = []

def get_weather(city_name):
    try:
        # Make the API request
        params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            # Extract relevant weather information
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {description}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("Failed to fetch weather data. Please check the city name or API key.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_favorite_city(city_name):
    if city_name not in favorite_cities:
        favorite_cities.append(city_name)
        print(f"{city_name} added to favorites.")
    else:
        print(f"{city_name} is already in your favorites.")

def remove_favorite_city(city_name):
    if city_name in favorite_cities:
        favorite_cities.remove(city_name)
        print(f"{city_name} removed from favorites.")
    else:
        print(f"{city_name} is not in your favorites.")

def list_favorite_cities():
    if favorite_cities:
        print("Your favorite cities:")
        for city in favorite_cities:
            print(city)
    else:
        print("You have no favorite cities yet.")

def auto_refresh_weather(city_name):
    while True:
        get_weather(city_name)
        time.sleep(15 + (15 * (time.time() % 2)))

if __name__ == "__main__":
    while True:
        print("Options:")
        print("1. Check weather by city name")
        print("2. Add a favorite city")
        print("3. Remove a favorite city")
        print("4. List favorite cities")
        print("5. Auto-refresh weather for a city")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            city_name = input("Enter a city name: ")
            get_weather(city_name)
        elif choice == '2':
            city_name = input("Enter a city name to add to favorites: ")
            add_favorite_city(city_name)
        elif choice == '3':
            city_name = input("Enter a city name to remove from favorites: ")
            remove_favorite_city(city_name)
        elif choice == '4':
            list_favorite_cities()
        elif choice == '5':
            city_name = input("Enter a city name for auto-refresh: ")
            auto_refresh_weather(city_name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
