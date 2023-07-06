import requests
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
import os
class FlightSearch:
    #https://partners.kiwi.com/
    def __init__(self):
        self.token = os.environ["tequila_token"]
        self.url = "https://api.tequila.kiwi.com/locations/query?"
        self.sheet = DataManager()
        self.prices = FlightData()
        self.sms = NotificationManager()
    def get_IATA_code(self):
        data = self.sheet.get_sheet_data()
        for row in data["prices"]:
            print(row["city"])
            header = {
                "apikey": self.token
            }
            query = {
                "term": row["city"],
                "locale": "en-US",
                "location_types": "airport",
                "active_only": "true"
            }
            response = requests.get(url=self.url, headers=header, params=query)
            data = response.json()
            city_IATA_code = data["locations"][0]["city"]["code"]
            self.sheet.update_row(row_id=row["id"], iata=city_IATA_code)
            flightinfo = self.prices.get_flight_price(iata=city_IATA_code)
            print(flightinfo)
            if flightinfo["price"] <= row["lowestPrice"]:
                self.sms.sendSMS(price=flightinfo["price"], from_airport=flightinfo["from_airport"], destination_airport=flightinfo["destination_airport"], departure_date=flightinfo["departure_date"], return_date=flightinfo["return_date"])
            elif flightinfo["price"] > row["lowestPrice"]:
                print("expensive")

