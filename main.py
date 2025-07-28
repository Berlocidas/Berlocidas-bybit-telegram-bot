import os
import requests
from telegram import Bot
from pybit import HTTP

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")

bot = Bot(token=TOKEN)
client = HTTP(api_key=BYBIT_API_KEY, api_secret=BYBIT_API_SECRET)

def get_price(symbol="ETHUSDT"):
    data = client.latest_information_for_symbol(symbol=symbol)
    return float(data["result"][0]["last_price"])

def send_signal():
    price = get_price()
    message = f"ETH/USDT kaina šiuo metu: {price}"
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    send_signal()
    bot.send_message(chat_id=CHAT_ID, text="Botas paleistas sėkmingai!")
