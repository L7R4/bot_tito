from telegram.ext import Updater, MessageHandler,Filters

#Funcion donde se reenvia el mensaje
def process_message(update,context):

    text = update.message.text
    id_origin_chat= update.message.chat.id

    if str(id_origin_chat) == "-688891110":
        context.bot.send_message(
        chat_id = "-626626137",
        text =  text
        )


def run():
    #Donde colocar el token
    updater = Updater(token="YOUR_TOKEN", use_context = True) 

    #El dispacher para poder utilizar toda la informacion que pasa por el update
    dp = updater.dispatcher 

    #Donde se agrega un manejador de mensajes con el callback de la funcion de arriba
    dp.add_handler(MessageHandler(filters=Filters.all ,callback=process_message)) 

    #Para que el bot una vez iniciado no se detenga
    updater.start_polling() 
    print("Bot is polling")
    updater.idle()


if __name__ == "__main__":
    run()
