from twilio.rest import Client
import smtplib
import os

class NotificationManager:
    '''This class is responsible for sending notifications with the deal flight details.'''
    def __init__(self):
        self.account_sid = os.environ.get("Acc-Sid")
        self.auth_token = os.environ.get("Auth-Token")
        self.my_email = os.environ.get("Email")
        self.password = os.environ.get("Password")

    def sendNotification(self, msg: str):
        '''Send message to myself to Phone Number'''
        if not bool(msg):
            return None
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=f"Low Price Alert!\n{msg}",
            from_= os.environ.get('from-Phone'),
            to= os.environ.get('to-Phone')
        )
        print(message.sid)

    def sendMail(self, msg: str, email:str):
        '''Send mails to all the users registered'''

        if not bool(msg):
            return None
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=email,
                msg=f"Subject:Low Price Alert!\n\n{msg}"
            )
