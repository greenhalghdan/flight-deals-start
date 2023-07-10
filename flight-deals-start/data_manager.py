import requests
import os

usersURL = "https://api.sheety.co/8af00e58daf0746f6934be397afa9f04/flightDeals/users"
class DataManager:

    def __init__(self):
        self.url = "https://api.sheety.co/8af00e58daf0746f6934be397afa9f04/flightDeals/prices"
        self.header = {
            "Authorization": os.environ["sheety_token"],
            "Content-Type": "application/json"
        }
        #self.updateurl = "https://api.sheety.co/8af00e58daf0746f6934be397afa9f04/flightDeals/prices/10"
        self.updateurl = f"https://api.sheety.co/8af00e58daf0746f6934be397afa9f04/flightDeals/prices/"


        #data = self.get_sheet_data()

    def get_sheet_data(self):
        response = requests.get(url=self.url, headers=self.header)
        d = response.json()
        return d

    def update_row(self, row_id, iata):
        content = {
            "price":
                {
                  "iataCode": iata
                },
            }
        response = requests.put(url=f"{self.updateurl}/{row_id}", headers=self.header, json=content)
        #response = requests.delete(url=self.updateurl)
        response.raise_for_status()

    def user_input(self, first_name, last_name, email_address):
        response = requests.get(url=usersURL, headers=self.header)
        current_users = response.json()
        for row in current_users["users"]:
            if email_address == row["email"]:
                return "You have already signed up!"
        userdata = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email_address
            }
        }
        response = requests.post(url=usersURL, headers=self.header, json=userdata)
        response.raise_for_status()
        return "You have been signed up!"

