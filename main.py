from telegram.ext import Updater, MessageHandler,Filters

#Funcion donde se reenvia el mensaje
def process_message(update,context):

    message = update.channel_post.message_id
    id_origin_chat= update.channel_post.chat.id

    if str(id_origin_chat) == "ORIGIN_CHAT_ID":
        context.bot.copy_message(
        chat_id = "RECEIVER_CHAT_ID",
        from_chat_id = "ORIGIN_CHAT_ID",
        message_id = message
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
    updater.idle()


if __name__ == "__main__":
    run()
