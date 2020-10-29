from pyrogram import Client
from os import environ
from dotenv import load_dotenv
load_dotenv()

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]

with Client(":memory:", api_id, api_hash) as app:
    print(app.export_session_string())
