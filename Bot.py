from telegram import Update

import telebot, wikipedia, re
import time
import os
from fuzzywuzzy import fuzz

# Создаем экземпляр бота
f = open('C:/Users/Anton/Desktop/token.txt', 'r')
token_in = f.read()
bot = telebot.TeleBot(token_in)




