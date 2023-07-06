from twilio.rest import Client
import os

class NotificationManager:
    # Twilio SMS API - https://www.twilio.com/docs/sms
    def __init__(self):
        self.account_sid = os.environ["account_sid"]
        self.auth_token = os.environ["auth_token"]
    def sendSMS(self, price, from_airport, destination_airport, departure_date, return_date):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=f"Low price alert: Only £{price} to fly from {from_airport} to {destination_airport}, from {departure_date}, to {return_date}",
            from_='+447723613314',
            to=os.environ["phone_number"]
        )
        print(message.status)

