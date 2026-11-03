import twilio
import os
import dotenv
from twilio.rest import Client

dotenv.load_dotenv()

# api_key = os.environ["TWILIO_API_KEY"]
auth_token = os.getenv["AUTH_TOKEN"]
account_sid = os.getenv["ACCOUNT_SID"]


client = Client(auth_token, account_sid)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_="+17372508034",
    to="8001676280",
)

print(message.body)