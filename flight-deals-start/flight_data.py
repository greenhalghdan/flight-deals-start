import requests
import datetime as dt
import os
class FlightData:
    def __init__(self):
        self.tequila_url = "https://api.tequila.kiwi.com/v2/search"
        self.tequila_token = os.environ["tequila_token"]
        self.header = {
            "apikey": self.tequila_token,
            "Content-Type": "application/json"
        }
        self.stopovers = 0
        self.stops = 0

    def get_flight_price(self, iata):
        tomorrow_date = dt.date.today() + dt.timedelta(days=1)
        six_months_date = tomorrow_date + dt.timedelta(days=(30 * 6))
        self.params = {
            "fly_from": "LON",
            "fly_to": iata,
            "date_from": tomorrow_date.strftime("%d/%m/%Y"),
            "date_to": six_months_date.strftime("%d/%m/%Y"),
            "vehicle_type": "aircraft",
            "sort": "price",
            "limit": "1",
            "curr": "GBP",
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "max_stopovers": self.stopovers,
        }
        response = requests.get(url=self.tequila_url, params=self.params, headers=self.header)
        response.raise_for_status()
        data = response.json()
        try:
            message = f'Low price alert: Only £{data["data"][0]["price"]} ' \
                      f'to fly from {data["data"][0]["route"][0]["flyFrom"]} ' \
                      f'to {data["data"][0]["route"][0]["flyTo"]} ' \
                      f'on {data["data"][0]["route"][0]["local_departure"]} ' \
                      f'returning {data["data"][0]["route"][1]["local_departure"]}'
        except IndexError:
            self.stops = 1
            self.stopovers = "2"
            self.params = {
                "fly_from": "LON",
                "fly_to": iata,
                "date_from": tomorrow_date.strftime("%d/%m/%Y"),
                "date_to": six_months_date.strftime("%d/%m/%Y"),
                "vehicle_type": "aircraft",
                "sort": "price",
                "limit": "1",
                "curr": "GBP",
                "nights_in_dst_from": "7",
                "nights_in_dst_to": "28",
                "max_stopovers": self.stopovers,
            }
            response = requests.get(url=self.tequila_url, params=self.params, headers=self.header)
            response.raise_for_status()
            data = response.json()
            # trip_info = {
            #     "price": data["data"][0]["price"],
            #     "from_airport": data["data"][0]["route"][0]["flyFrom"],
            #     "destination_airport": data["data"][0]["route"][3]["flyTo"],
            #     "departure_date": data["data"][0]["route"][0]["local_departure"],
            #     "return_date": data["data"][0]["route"][3]["local_departure"],
            #     "lay_over": data["data"][0]["route"][0]["flyTo"],
            # }
            message = f'Low price alert: Only £{data["data"][0]["price"]} ' \
                      f'to fly from {data["data"][0]["route"][0]["flyFrom"]} to {data["data"][0]["route"][0]["flyTo"]}' \
                      f' on {data["data"][0]["route"][0]["local_departure"]} ' \
                      f'returning {data["data"][0]["route"][1]["local_departure"]} ' \
                      f'with a lay over in {data["data"][0]["route"][0]["flyTo"]}'
        return data["data"][0]["price"], message
