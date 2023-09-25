import requests
from datetime import datetime, timedelta
import numpy as np



current_date = datetime.now()

one_week_from_now = current_date + timedelta(7)

current_day_str = current_date.strftime("%Y-%m-%d")
one_week_from_now_str = one_week_from_now.strftime("%Y-%m-%d")

# Get today's date
today = datetime.now().date()
# Create a list with today and the next 7 days
dates_list = [today + timedelta(days=i) for i in range(8)]

api_url = f"https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&hourly=temperature_2m&start_date={current_day_str}&end_date={one_week_from_now_str}"

print(api_url)

tempDayHighest = []

try:
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        
        temp_array = data["hourly"]["temperature_2m"]
        hourly_array = data["hourly"]["time"]

        max_temp = np.max(temp_array)
        max_temp_index = np.where(temp_array == max_temp)[0][0]


        print(f"The highest temperature is {max_temp}°C at {hourly_array[max_temp_index]}")

    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")