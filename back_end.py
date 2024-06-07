import requests
import os
API_KEY="28fe4fd71d74f3ab6d152c5f99dd0417"
#cityname="Delhi"
def get_data(place,forecast_days):
        url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
        response=requests.get(url)
        data=response.json()
        filter_data=data["list"]
        nr_values=8*forecast_days
        filter_data=filter_data[:nr_values]
        return filter_data


if __name__=="__main__":
    get_data(place="london",forecast_days=3)

