# Weather Alert Script

This Python script periodically checks the weather forecast for a specified location and sends an SMS alert if rain is expected within the next 12 hours. It is designed to run on **PythonAnywhere** or a similar cloud platform on a daily basis.

## Features

- Retrieves weather data from the **OpenWeatherMap** API.
- Sends SMS notifications via **Twilio**.
- Secures sensitive data using environment variables.
- Set up for periodic execution using cloud services like **PythonAnywhere**.

## Requirements

- Python 3.x
- [Requests](https://pypi.org/project/requests/) - For making HTTP requests.
- [Twilio](https://pypi.org/project/twilio/) - For sending SMS notifications.

If you don't have Twilio account, first you need to create one and get get authentication codes [here](https://www.twilio.com/en-us).

Then, you can install the required packages using pip:
```bash
pip install requests twilio
```

## Environment Variables
Ensure the following environment variables are set on your PythonAnywhere or local environment for the script to function correctly:

- `API_KEY`: Your OpenWeatherMap API key.
- `ACC_SID`: Twilio account SID.
- `AUTH_TOKEN`: Twilio authentication token.
- `FROM_NUM`: Twilio number used to send the alert.
- `USER_NUM`: User's number to receive the alert.

You can set these in PythonAnywhere via the **Environment Variables** settings, or in your local environment using the following commands (for Linux/macOS):
```bash
export API_KEY="your_openweathermap_api_key"
export ACC_SID="your_twilio_account_sid"
export AUTH_TOKEN="your_twilio_auth_token"
export FROM_NUM="twilio_phone_number"
export TO_NUM="user's_phone_number"
```

## Deployment on PythonAnywhere

1. Upload the script to your PythonAnywhere account.
2. Set up the required environment variables under the "Web" or "Tasks" tab.
3. Schedule the script to run daily using the "Tasks" section.

## Acknowledgments
This project is a part of the course "100 Days of Code: The Complete Python Pro Bootcamp", taught by Dr. Angela Yu on Udemy.

## Author

[mdgolamfardin](https://github.com/mdgolamfardin)