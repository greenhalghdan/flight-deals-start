#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
data = DataManager()
print(data.get_sheet_data())
search = FlightSearch()
print(data.get_sheet_data())
search.get_IATA_code()
prices = FlightData()
# flightinfo = prices.get_flight_price()
# print(flightinfo)
