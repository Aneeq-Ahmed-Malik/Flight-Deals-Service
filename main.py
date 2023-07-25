from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

search = FlightSearch()
data = DataManager()
data_flight = FlightData()
notification = NotificationManager()

# Populating IATA codes for all cities
city_list = data.get_cities()
iata_list = [search.get_IATA(city) for city in city_list]
data.upload_IATA(iata_list)

# Registering Users to the Flight Club
print("Welcome to Aneeq's Flight Club!")
choice = input("Want to register or Already registered (Y/N) ? ")

if choice.lower() == "y":
    firstName = input("Enter your first Name : ").title()
    lastName = input("Enter your last Name : ").title()
    email = input("Enter your Email : ").lower()
    data.register_user(firstName, lastName, email)
    print("Congratulations! you've been registered as user!")

print("You'll be notified of exciting flight deals!")

codes = data.get_iata()
prices = data.get_price()
emails = data.get_email()

for (code,price) in zip(codes,prices):
    flight = search.get_flights(code, price)
    details = data_flight.parse_data(flight)
    for email in emails:
        notification.sendMail(details, email)
