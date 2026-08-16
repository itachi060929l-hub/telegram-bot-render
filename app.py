import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

app = Flask(__name__)

TOKEN = "8778899800:AAENMYdLSIRQ2T6J1wjyRZCh8uDYhRalkBM"

# Khởi tạo bot
bot = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot đang chạy!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Bạn nói: {update.message.text}")

bot.add_handler(CommandHandler("start", start))
bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

@app.route('/')
def home():
    return "Bot is running!", 200

if __name__ == "__main__":
    # Chạy bot polling trong cùng tiến trình (không dùng thread)
    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(bot.run_polling())
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
