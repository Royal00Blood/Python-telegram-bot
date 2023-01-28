from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

f = open('C:/Users/Anton/Desktop/token.txt', 'r')
token_in = f.read()
updater = Updater(token_in)

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))


print('server start')
updater.start_polling()
updater.idle()