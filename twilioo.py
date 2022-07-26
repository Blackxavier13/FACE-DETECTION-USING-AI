from twilio.rest import Client
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Your Account SID from twilio.com/console
account_sid = "AC51902da0eb1d0ce458a1b9ddf58f7015"
# Your Auth Token from twilio.com/console
auth_token  = "925e392cdf76daa7b6b8dea02d6acda6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919597302419", 
    from_="+15865542681",
    body= current_time)

print(message.sid)
