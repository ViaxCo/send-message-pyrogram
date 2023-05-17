# A script to use pyrogram module to send messages to telegram users periodically using pyrogram
# The PyPi schedule module can be used to achieve this or the inbuilt time module
import schedule
import time
from pyrogram import Client
# For environment variables
from os import environ
from dotenv import load_dotenv
load_dotenv()

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
session_string = environ["SESSION_STRING"]

app = Client(session_string, api_id, api_hash)

with app:
    open("contacts.json", "w")
    f = open("contacts.json", "a", encoding="utf-8")
    f.write(str(app.get_contacts()))
    f.close()
