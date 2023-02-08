##pasiimti info, pagal info issiust sms
import requests
from datetime import datetime
from twilio.rest import Client


def send_SMS(message):
    account_sid = "AC4f6db1384a4d36317dcb42b426f91bf1"
    auth_token = "fe382b3acc6edefba5cd293bfd7559de"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='+19706717541',
        to='+37068343874'
    )

# date = datetime.today().strftime('%Y-%m-%d')
# x = requests.get('https://api.open-meteo.com/v1/forecast?latitude=54.69&longitude=25.28&hourly=rain&start_date={}&end_date={}'.format(date,date))
x = requests.get('https://api.open-meteo.com/v1/forecast?latitude=54.69&longitude=25.28&hourly=rain&start_date=2022-09-28&end_date=2022-09-28')
res = x.json()

time = res["hourly"]["time"]
rain = res["hourly"]["rain"]

data = {}
for i,v in enumerate(time):
    data[time[i]] = rain[i]

rainy_times = {}

for i,v in data.items():
    if v >= 1.0:
        rainy_times[i] = v

if rainy_times:
    message = 'Lyja lietus per karaliaus pietus :p\n{time}'.format(time = '\n'.join([i.split('T')[1] for i in rainy_times.keys()]))
    # print(message)
    send_SMS(message)


