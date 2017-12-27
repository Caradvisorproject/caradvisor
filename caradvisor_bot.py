import logging
import datetime

from settings import TELEGRAM_API_KEY

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from get_weather import get_weather_data, get_weather_message
from roads_closed import get_road_restrictions

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    # filename='bot.log'
                    )



def caradvice(bot, update):
    #print(update)
    logging.info('User {} pushed /caradvice'.format(update.message.chat.username))
    user_info_text = "Hello, {}! Command is {}".format(update.message.chat.first_name, '/caradvice')

    caradvisor_weather_message = get_weather_message()
    caradvisor_closed_roads_message = get_road_restrictions()

    update.message.reply_text(user_info_text)
    update.message.reply_text(caradvisor_weather_message)
    update.message.reply_text(caradvisor_closed_roads_message)

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
