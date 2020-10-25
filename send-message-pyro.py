from pyrogram import Client
import time

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
session_string = environ["SESSION_STRING"]

app = Client(session_string, api_id, api_hash)

with app:
    n = 0
    while n < 4:
        # Send message with 5 seconds interval
        print("Waiting...")
        time.sleep(5)
        
        app.send_message("me", f"Heroku test no. {n}...")
        print("Message sent successfully!")
        n += 1
