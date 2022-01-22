from telegram.ext import Updater, MessageHandler,Filters

def process_message(update,context):

    text = update.message.text
    id_origin_chat= update.message.chat.id

    if str(id_origin_chat) == "-688891110":
        context.bot.send_message(
        chat_id = "-626626137",
        text =  text
        )


def run():
    updater = Updater(token="YOUR_TOKEN", use_context = True)

    
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.all ,callback=process_message))

    updater.start_polling()
    print("Bot is polling")
    updater.idle()


if __name__ == "__main__":
    run()
