import os
from pyrogram import Client

from pyrogram import pyrogram
from pyrogram.sessions import StringSession


api_id = int(os.environ.get('API_ID') or input("Enter your API_ID: "))
api_hash = os.environ.get('API_HASH') or input("Enter your API_HASH: ")

app = Client("my_account")

with app:

    print(app.export_session_string())
