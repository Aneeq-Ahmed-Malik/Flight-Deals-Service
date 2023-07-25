import requests
import os

class DataManager:
    '''This class is responsible for talking to the Google Sheet.'''

    def __init__(self):
        self.getAPI = "https://api.sheety.co/4376a327bdce5cd0d6a23f258a1b9588/flightDeals/prices"
        self.putAPI = "https://api.sheety.co/4376a327bdce5cd0d6a23f258a1b9588/flightDeals/prices"
        self.postAPI = "https://api.sheety.co/4376a327bdce5cd0d6a23f258a1b9588/flightDeals/users"
        self.header = {
            "Authorization" : os.environ.get("Auth")
        }

    def get_cities(self) -> list:

        response = requests.get(self.getAPI, headers=self.header)
        print(response.json())
        data = response.json()['prices']
        cities = [record['city'] for record in data]
        return cities

    def upload_IATA(self, codes: list):
        row = 2
        for code in codes:
            parameters = {
                'price': {
                    'iataCode': code
                }
            }
            response = requests.put(f"{self.putAPI}/{row}", json=parameters, headers=self.header)
            response.raise_for_status()
            row += 1

    def get_iata(self) -> list:
        response = requests.get(self.getAPI, headers=self.header)
        data = response.json()['prices']
        codes = [record['iataCode'] for record in data]
        return codes

    def get_price(self) ->list:
        response = requests.get(self.getAPI, headers=self.header)
        data = response.json()['prices']
        prices = [record['lowestPrice'] for record in data]
        return prices

    def register_user(self, first_name, second_name, email):
        parameters = {
            'user' : {
                "firstName" : first_name,
                "lastName" : second_name,
                "email" : email
            }
        }
        response = requests.post(self.postAPI, headers=self.header, json=parameters)
        response.raise_for_status()

    def get_email(self):

        response = requests.get("https://api.sheety.co/4376a327bdce5cd0d6a23f258a1b9588/flightDeals/users", headers=self.header)
        data = response.json()['users']
        emails = [record['email'] for record in data]
        return emails
