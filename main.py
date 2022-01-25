from socket import timeout
from telegram.ext import Updater, MessageHandler,Filters

#Funcion donde se reenvia el mensaje
def process_message(update,context):

    message = update.channel_post.message_id
    id_origin_chat= update.channel_post.chat.id

    if str(id_origin_chat) == "-1001659970909":
        context.bot.copy_message(
        chat_id = -1001355916451,
        from_chat_id = -1001659970909,
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
    print("Bot is polling")
    updater.idle()


if __name__ == "__main__":
    run()
