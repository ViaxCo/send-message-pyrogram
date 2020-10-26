from pyrogram import Client
import time

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
session_string = environ["SESSION_STRING"]

app = Client(session_string, api_id, api_hash)

with app:
    n = 0
    while n < 3:
        # Send message with 10 minutes interval
        print("Waiting...")
        time.sleep(600)
        
        app.send_message("me", f"Heroku test no. {n}...")
        print("Message sent successfully!")
        n += 1
