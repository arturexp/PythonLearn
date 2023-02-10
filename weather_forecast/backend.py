import requests


API_KEY = '1c77608bb70038353eef08e106182b21'


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json

    return data


if __name__ == "__main__":
    print(get_data(place="Moscow"))
