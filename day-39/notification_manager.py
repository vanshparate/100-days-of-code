from twilio.rest import Client

account_sid = ''
auth_token = ''
virtual_number = ''
verified_number = ''


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=virtual_number,
            to=verified_number
        )
        print(message.sid)
