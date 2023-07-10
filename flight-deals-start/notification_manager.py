from twilio.rest import Client
import os
import smtplib
class NotificationManager:
    # Twilio SMS API - https://www.twilio.com/docs/sms
    def __init__(self):
        self.account_sid = os.environ["account_sid"]
        self.auth_token = os.environ["auth_token"]
    def sendSMS(self, body):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=body,
            from_='+447723613314',
            to=os.environ["phone_number"]
        )
        print(message.status)

