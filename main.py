import requests
from twilio.rest import Client
import os

rec_twilio = os.environ.get('REC_TWILIO')


# OpenWeatherMap API endpoint for 5-day weather forecast (in 3-hour intervals, total of 40 reports)
OWM_endpoint = f"https://api.openweathermap.org/data/2.5/forecast"

# API key for OpenWeatherMap, retrieved from environment variables for security
api_key = os.environ.get('API_KEY')

# Twilio account SID and authentication token, also retrieved from environment variables for security
account_sid = os.environ.get('ACC_SID')
auth_token = os.environ.get('AUTH_TOKEN')

# Parameters for the weather API request, specifying the latitude and longitude for Halifax, and limiting the results to 4 intervals (12 hours)
weather_params = {
    "lat": 44.65,
    "lon": 63.58,
    "appid": api_key,
    "cnt": 4
}

# Making a GET request to the OpenWeatherMap API with the specified parameters
response = requests.get(url=OWM_endpoint, params=weather_params)

# Parsing the JSON response from the API
data = response.json()
print(data)

# Extracting the weather information from the response
weather_list = data['list']

# List of weather condition codes indicating rainy weather (codes less than 800 indicate precipitation)
rainy_weather_condition_codes = [day['weather'][0]['id'] for day in weather_list if day['weather'][0]['id'] < 800]

# If there are any rainy weather conditions in the forecast, send an SMS alert using Twilio
if len(rainy_weather_condition_codes) > 0:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=os.environ.get('FROM_NUM'),        # Twilio phone number to send the message from
        to=os.environ.get('USER_NUM'),
        body="It's gonna rain today, bring an umbrella."  # SMS message content
    )
    print(message.status)  # Print the status of the sent message

