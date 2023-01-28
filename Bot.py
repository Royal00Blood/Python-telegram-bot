import telebot, wikipedia, re
import time
import os


# Создаем экземпляр бота
f = open('C:/Users/Anton/Desktop/token.txt', 'r')
token_in = f.read()
bot = telebot.TeleBot(token_in)




