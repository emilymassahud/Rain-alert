import requests
from twilio.rest import Client
import os

api_key = os.environ.get('API_KEY')
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
FROM_NUMBER = os.environ.get('FROM_NUMBER')
TO_NUMBER = os.environ.get('TO_NUMBER')
MY_LAT = '43.6'
MY_LONG = '-75.13'
APP_ID = os.environ.get('APP_ID')
URL = f'https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LONG}&exclude=current,minutely,daily&appid={APP_ID}'


response = requests.get(url=URL)
response.raise_for_status()
# print(response.json())
weather_data = response.json()
rain = False

# Could also have used the command slice [:] for the range of hours from the list hourly
for i in range(0, 11):
    weather_code = response.json()['hourly'][i]['weather'][0]['id']
    if weather_code < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
             body="It's going to rain today, bring an umbrella!.",
             from_=FROM_NUMBER,
             to=TO_NUMBER
         )

    print(message.status)

