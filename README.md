# send-message-pyrogram

A python script used to automatically send/schedule messages to users periodically using the [Pyrogram](https://github.com/pyrogram/pyrogram) framework for Telegram, the [schedule](https://schedule.readthedocs.io/en/stable/) and [time](https://docs.python.org/3/library/time.html) modules.

## Installation

### Simple installation

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ViaxCo/send-message-pyrogram/tree/main)

### Manual installation

You can clone the repo:

```bash
git clone https://github.com/ViaxCo/send-message-pyrogram.git
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

On your local system, you can create a `.env` file to store your environment variables; `API_ID`, `API_HASH` and `SESSION_STRING`. These will then be loaded by the `python-dotenv` module.

To generate the `session_string`, run:

```bash
python3 GenerateSessionString.py
```

This will lead you to input your phone number and authenticate yourself with Telegram if you haven't already, and proceed to print your session string, which you should copy and place in the `SESSION_STRING` variable in your `.env` file.

## How to use

You can run the program using:

```bash
python3 send-message-pyrogram.py
```

To change the receiver of the message, simply change "me" to the id or name of the contact you wish to send the message to:

```bash
app.send_message("me", "Your message")
```

### To change frequency of the messages

#### Using the time module

##### Example

```python
#USING THE INBUILT TIME MODULE
with app:
    n = 0
    while n < 3:
        # Send message with 10 minutes interval
        app.send_message("me", "Your message")
        print("Message sent successfully!")
        print("Waiting...")
        time.sleep(600)
        n += 1
```

This sends the message 3 times with 10 minutes interval. The number of times the message should be sent can be changed by changing the number: `n < 3`. The time interval between messages can be changed by changing the number appropriately in seconds: `time.sleep(600)`.

#### Using the schedule module

##### Example

```python
# USING THE SCHEDULE MODULE
n = 0


def job():
    global n
    app.send_message("me", "Your message")
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
            break
```

This sends a message 18 times with 30 minutes interval. The number of times the message should be sent can be changed by changing the number: `if n == 18`. The time interval between messages can be changed by changing the values of `schedule.every()...` as needed.

## Notice about the schedule module

When deployed remotely on somewhere like Heroku, note that Heroku's servers use UTC+0, so every time value you explicitly set should be in UTC+0 to match your time zone.
Also, for times with single digit hours such as "7:15", make sure to add a leading zero: "07:15".

**Enjoy!**
