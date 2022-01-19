from lib2to3.pgen2 import token
from telegram.ext import Updater, CommandHandler

def start(update,context):
    update.message.reply_text("Hola pibe")

if __name__ == "__main__":
    updater = Updater(token="YOUR_TOKEN", use_context = True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start))

    updater.start_polling()
    updater.idle()