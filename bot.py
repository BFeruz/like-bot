from settings import get_token
from telegram.ext import (
    Updater, 
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)
from handlers import (
    start,
    like, dislike,
    inline_like,
)


def main():
    TOKEN = get_token()

    # create udpater obj
    updater = Updater(TOKEN)
    
    # create dispatcher obj
    dispatcher = updater.dispatcher
    
    # add command handlers
    dispatcher.add_handler(handler=CommandHandler(command='start', callback=start))
    
    # add message handlers
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('👍'), callback=like))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('👎'), callback=dislike))
    
    # add calback_query handlers
    dispatcher.add_handler(handler=CallbackQueryHandler(callback=inline_like, pattern='inline_like'))
    # dispatcher.add_handler(handler=CallbackQueryHandler(filters=Filters.text('👎'), callback=dislike))

    # start polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
