# Activity6
# Vahini Madipalli
# Course: ISQA3900-850: Web Application Development
# Working with JSON and weather API

from datetime import datetime
import requests
import pytemperature
from datetime import date

# Function to display the current date
now = date.today()
now = now.strftime("%A, %B %d, %Y")
print("ISQA 3900 Open Weather API")
print(now)
print()

# Enter the loop below if the user enter y to continue
choice = "y"
while choice.lower() == "y":

    # Prompt user to enter city and country code
    city = input("Enter city: ")
    print("Use ISO letter country code like: https://countrycode.org/")
    country = input("Enter country code: ")
    api_start = 'https://api.openweathermap.org/data/2.5/weather?q='
    api_key = '&appid=bc7b85d10431e095b2d86ca3c44f5197'
    url = api_start + city + ',' + country + api_key
    json_data = requests.get(url).json()

    # exceptional handling to handle invalid entries for city and country
    try:
        weather_description = json_data['weather'][0]['description']
        print("Current conditions: ", weather_description)

        # converting kelvin to fahrenheit
        current_temp = json_data['main']['temp']
        current_temp = pytemperature.k2f(current_temp)
        print("Current Temperature in Fahrenheit:   " + str(current_temp))

        current_pressure = json_data['main']['pressure']
        print("Current Pressure in hpa:   " + str(current_pressure))

        current_humidity = json_data['main']['humidity']
        print("Current Humidity:   " + str(current_humidity) + "%")

        # converting kelvin to fahrenheit
        expected_low_temp = json_data['main']['temp_min']
        expected_low_temp = pytemperature.k2f(expected_low_temp)
        print("Expected Low Temperature in Fahrenheit:   " + str(expected_low_temp))

        expected_high_temp = json_data['main']['temp_max']
        expected_high_temp = pytemperature.k2f(expected_high_temp)
        print("Expected High Temperature in Fahrenheit:   " + str(expected_high_temp))

        choice = input("Continue (y/n)?: ")
        print()

    except:
        print("      Unable to access " + city + " in " + country)
        print("      Verify city name and country code")

        # prompt user to continue to enter another city and country
        choice = input("Continue (y/n)?: ")
print('Bye')
