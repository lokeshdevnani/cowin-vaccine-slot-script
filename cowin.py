import requests
import datetime
import json
import os
from time import sleep

def notify(title, text):
    os.system("""
              osascript -e 'display alert "{}" message "{}"'
              """.format(title, text))

def process(days, district_ids, age, availability_threshhold):
    date_today = datetime.datetime.today()
    date_list = [date_today + datetime.timedelta(days=x) for x in range(numdays)]
    date_str_list = [x.strftime("%d-%m-%Y") for x in date_list]

    for district_id in district_ids:
        for date in date_str_list:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district_id, date)
            response = requests.get(URL)
            if response.ok:
                resp_json = response.json()
                for center in (resp_json["centers"] or []):
                    for session in center["sessions"]:
                        if session["min_age_limit"] <= age and session["available_capacity"] > availability_threshhold:
                            message = '({}) {} [{}] Date: {}, Price: {}'.format(center["pincode"], center["name"], session["available_capacity"], session["date"], center["fee_type"])
                            notify("Vaccine Available! GoCoronaGo!", message)
                            print("Available: ", message)


numdays = 3
age = 25
district_ids = [265, 294] #265: Bangalore Urban, 294: BBMP
sleep_time = 10
availability_threshhold = 10

for i in range(0, 5):
    process(numdays, district_ids, age, availability_threshhold)
    sleep(sleep_time)
