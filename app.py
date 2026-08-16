import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

app = Flask(__name__)

# === TOKEN CỦA BẠN (đã điền sẵn) ===
TOKEN = "8967046077:AAEOVWzXiVjTGCSQFrE-Gf5pwounSysejlY"

# Khởi tạo bot
bot_app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot đang chạy trên Render!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Bạn nói: {update.message.text}")

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

def run_bot():
    print("Bot đang chạy polling...")
    bot_app.run_polling()

@app.route('/')
@app.route('/health')
def health():
    return "Bot is running!", 200

if __name__ == "__main__":
    thread = threading.Thread(target=run_bot)
    thread.start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)