import requests
import datetime as dt
import os

class FlightSearch:
    '''This class is responsible for talking to the Flight Search API.'''

    def __init__(self):
        self.API = "https://api.tequila.kiwi.com"
        self.header = {
            "apikey" : os.environ.get("Key")
        }

    def get_IATA(self, city: str) -> str:
        parameters = {
            "term" : city,
            "location_types" : "city"
        }
        response = requests.get(f"{self.API}/locations/query", headers=self.header, params=parameters)
        response.raise_for_status()
        return response.json()['locations'][0]['code']


    def get_flights(self, city : str, price : int) -> dict:
        date = dt.datetime.now()
        last_date = date + dt.timedelta(days=180)

        parameters = {
            "fly_from" : "city:ISB",
            "fly_to" : city,
            "date_from" : date.strftime("%d/%m/%Y"),
            "date_to" : last_date.strftime("%d/%m/%Y"),
            "return_from" : date.strftime("%d/%m/%Y"),
            "return_to" : last_date.strftime("%d/%m/%Y"),
            "price_from" : 0,
            "price_to" : price,
            "sort" : "price",
            "curr" : "PKR"
        }

        response = requests.get(f"{self.API}/v2/search", headers=self.header, params=parameters)
        response.raise_for_status()
        try:
            return response.json()['data'][0]
        except IndexError:
            return {}
