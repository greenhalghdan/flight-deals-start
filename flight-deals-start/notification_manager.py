from twilio.rest import Client
import os
import smtplib
from data_manager import DataManager
class NotificationManager:
    # Twilio SMS API - https://www.twilio.com/docs/sms
    def __init__(self):
        self.account_sid = os.environ["account_sid"]
        self.auth_token = os.environ["auth_token"]
        self.recipients = DataManager()
    def sendSMS(self, body):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=body,
            from_='+447723613314',
            to=os.environ["phone_number"]
        )
        print(message.status)
    def sendEMail(self, body):
        users = self.recipients.get_recipients()
        for user in users:
            with smtplib.SMTP("eu-smtp-outbound-1.mimecast.com", 587) as connection:
                connection.starttls()
                connection.login(user=os.environ["email_user"], password=os.environ["email_password"])
                connection.sendmail(from_addr="noreply@suffolkmotorcyclespares.co.uk", to_addrs={user},
                                    msg=f"subject:Cheap Flight Deals\n\n{body.encode('utf-8')}")