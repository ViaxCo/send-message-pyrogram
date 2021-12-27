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

# USING THE INBUILT TIME MODULE
# with app:
#     n = 0
#     while n < 3:
#         # Send message with 10 minutes interval
#         app.send_message("me", f"Test no. {n}...")
#         print("Message sent successfully!")
#         print("Waiting...")
#         time.sleep(600)
#         n += 1


# USING THE SCHEDULE MODULE
n = 0


def job():
    global n
    app.send_message("2004144250", "lol")
    print("Message sent successfully!")
    print("Waiting...")
    n += 1


# schedule.every().day.at("10:30").do(job)
schedule.every(0.1).seconds.do(job)
# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

with app:
    while True:
        schedule.run_pending()
        time.sleep(1)
        if n == 18:
            app.send_message(
                "me", "This ran for 9 hours with a 30 minute interval and has now come to an end.")
            break
