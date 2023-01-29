############--Libraries--########################
import random
import telebot
from telebot import types  # для указание типов
import model as m
##################################################

# Создаем экземпляр бота
f = open('C:/Users/Anton/Desktop/token.txt', 'r')
token_in = f.read()
bot = telebot.TeleBot(token_in)

hi_ansver  = ["Привет!","Hi, amigos!","Ола,сеньер","🤝","✌🏻","👋🏻"]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("👼🏼 Выберите действие")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот ".format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text = random.choice(hi_ansver))
    elif (message.text == "👼🏼 Выберите действие"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👀 Найти сотрудника ")
        btn2 = types.KeyboardButton("👨🏻 ‍Сделать выборку сотрудников по должности")
        btn3 = types.KeyboardButton("🤑 Сделать выборку сотрудников по зарплате")
        btn4 = types.KeyboardButton("🧐 Добавить сотрудника")
        btn5 = types.KeyboardButton("😵 Удалить сотрудника")
        btn6 = types.KeyboardButton("🙈 Обновить данные сотрудника")
        btn7 = types.KeyboardButton("🙋🏻‍♂️Экспортировать данные в формате json")
        btn8 = types.KeyboardButton("🙋🏼 Экспортировать данные в формате csv")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        markup.add(btn5)
        markup.add(btn6)
        markup.add(btn7)
        markup.add(btn8)
        markup.add(back)
        bot.send_message(message.chat.id, text="👼🏼 Выберите действие", reply_markup=markup)

    elif (message.text == "👀 Найти сотрудника"):

        bot.send_message(message.chat.id, "АААА?")

    elif message.text == "👨🏻 ‍Сделать выборку сотрудников по должности":

        bot.send_message(message.chat.id, text="АААА?")

    elif (message.text == "🤑 Сделать выборку сотрудников по зарплате"):

        bot.send_message(message.chat.id, text="АААА?")

    elif message.text == "🧐 Добавить сотрудника":
        bot.send_message(message.chat.id, text='АААА?')


    elif message.text == "😵 Удалить сотрудника":
        bot.send_message(message.chat.id, text='АААА?')

    elif message.text == "🙈 Обновить данные сотрудника":
        bot.send_message(message.chat.id, text='АААА?')

    elif message.text == "🙋🏻‍♂️Экспортировать данные в формате json":
        bot.send_message(message.chat.id, text='Ваща база данных в формате json')
        bot.send_document(message.chat.id, open(r'data\data.json', 'rb'))
    elif message.text == "🙋🏼 Экспортировать данные в формате csv":
        bot.send_message(message.chat.id, text='Ваща база данных в формате csv')
        bot.send_document(message.chat.id, open(r'data\data.csv', 'rb'))
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("👼🏼 Выберите действие")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)


# def add_new_worker(message):
#     flag = 1
#     if flag == 1:
#         bot.send_message(message.chat.id, text="Введите имя нового работника->")
#         name = message.text
#         flag+=1
#     elif flag==2:
#         bot.send_message(message.chat.id, text="Введите фамилию нового работника->")
#         surname = message.text
#         flag += 1
#     elif flag==3:
#         bot.send_message(message.chat.id, text="Введите отдел нового работника->")
#         department = message.text
#         flag += 1
#     elif flag==4:
#         bot.send_message(message.chat.id, text="Введите отдел нового работника->")
#         position = message.text
#         flag += 1
#     elif flag==5:
#         bot.send_message(message.chat.id, text="Введите отдел нового работника->")
#         salary = message.text
#         flag += 1
#     else:
#         flag = 0
#     return name, surname, department, position, salary