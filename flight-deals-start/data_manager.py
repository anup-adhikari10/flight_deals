import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/95eb99d1247bfe2a7cb77486ab4543c1/flightDeals/prices"

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=SHEETY_PRICES_ENDPOINT,auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                auth=self._authorization,
                json=new_data
            )
            print(response.text)