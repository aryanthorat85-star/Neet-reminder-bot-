 import os
import time
import schedule
from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Yeh token Telegram BotFather se milega
TOKEN = os.getenv("TELEGRAM_TOKEN") or "PUT_YOUR_TELEGRAM_BOT_TOKEN_HERE"
CHAT_ID = os.getenv("CHAT_ID") or "PUT_YOUR_CHAT_ID_HERE"

bot = Bot(token=TOKEN)

def send_reminder():
    bot.send_message(chat_id=CHAT_ID, text="📚 Time to study, legend! NEET waits for no one 💪")

def start(update, context):
    update.message.reply_text("Hey bro, reminder bot is ON 🔥")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    # Reminder time set kar (example: har 2 ghante)
    schedule.every(2).hours.do(send_reminder)

    updater.start_polling()
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
