import logging
import datetime

from settings import TELEGRAM_API_KEY

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    # filename='bot.log'
                    )



def caradvice(bot, update):
    #print(update)
    logging.info('User {} pushed /caradvice'.format(update.message.chat.username))
    mytext = "Hello, {}! Command is {}".format(update.message.chat.first_name, '/caradvice')
    update.message.reply_text(mytext)

    print('started caradvice_bot')


def chat(bot, update):
    text = update.message.text
    logging.info(text)

    update.message.reply_text('Hellow!')



def main():
    upd = Updater(TELEGRAM_API_KEY)


    upd.dispatcher.add_handler(CommandHandler('caradvice', caradvice))
    upd.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    upd.start_polling()
    upd.idle()

if __name__ == '__main__':
    logging.info('Bot started')
    main()
