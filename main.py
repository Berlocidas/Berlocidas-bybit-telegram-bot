
import os
import requests
from telegram import Bot
from telegram.ext import Updater
from bybit import bybit

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

# Pavyzdinė žinutė
bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="Botas paleistas sėkmingai!")
