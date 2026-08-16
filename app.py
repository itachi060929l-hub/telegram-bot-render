import os
from flask import Flask, request, Response
import telegram
from telegram import Update

app = Flask(__name__)

TOKEN = "8778899800:AAENMYdLSIRQ2T6J1wjyRZCh8uDYhRalkBM"
bot = telegram.Bot(token=TOKEN)

@app.route('/')
def home():
    return "Bot is running!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        update = Update.de_json(data, bot)
        chat_id = update.message.chat.id
        text = update.message.text
        bot.send_message(chat_id=chat_id, text=f"Bạn nói: {text}")
        return Response("ok", status=200)
    except Exception as e:
        print(e)
        return Response("error", status=500)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
