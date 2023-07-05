import requests

class DataManager:

    def __init__(self):
        self.url = "https://api.sheety.co/8af00e58daf0746f6934be397afa9f04/flightDeals/prices"
        self.header = {
            "Authorization": "Bearer ksjdh;ksnh;gkljhnsdf;k;"
        }

    def get_sheet_data(self):
        response = requests.get(url=self.url, headers=self.header)
        print(response.json())