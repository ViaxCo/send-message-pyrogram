from pyrogram import Client
import time
import schedule

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
session_string = environ["SESSION_STRING"]

app = Client(session_string, api_id, api_hash)

# with app:
#     n = 0
#     while n < 3:
#         # Send message with 10 minutes interval
#         app.send_message("me", f"Heroku test no. {n}...")
#         
#         print("Message sent successfully!")
#         print("Waiting...")
#         time.sleep(600)
#         n += 1

###################################################################

n = 0


def job():
    global n
    app.send_message("me", f"Heroku test no. {n}...")
    print("Message sent successfully!")
    print("Waiting...")
    n += 1


# schedule.every().day.at("10:30").do(job)
# schedule.every(5).seconds.do(job)
schedule.every(30).minutes.do(job)
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
