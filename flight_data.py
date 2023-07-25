class FlightData:
    '''This class is responsible for sorting out the data for the flights'''

    def __init__(self):
        self.data = {
            "city_from" : "Islamabad-ISB",
            "city_to" : "",
            "date_from" : "",
            "date_to" : "",
            "price" : "",
            "stay" : ""

        }
        self.info = ""

    def parse_data(self, data: dict):
        if not bool(data):
            return None

        self.info = ""
        self.data['city_to'] = data['cityTo'] + "-" + data['cityCodeTo']
        self.data['date_from'] = data['route'][0]['local_arrival'].split("T")[0]
        self.data['date_to'] = data['route'][-1]['local_arrival'].split("T")[0]
        self.data['price'] = "Rs. " + "{:,.2f}".format(data['price']) + "/-"
        self.data['stay'] = data['nightsInDest']
        self.info = f"Only {self.data['price']} from {self.data['city_from']} to {self.data['city_to']}, with a stay of " \
                    f"{self.data['stay']} nights, from {self.data['date_from']} to {self.data['date_to']}."
        return self.info

