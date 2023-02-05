############--Libraries--########################
import random
import telebot
from telebot import types  # для указание типов
import model as m
import requests
from pprint import pprint

##################################################

# Создаем экземпляр бота
f = open('C:/Users/Anton/Desktop/token.txt', 'r')
token_in = f.read()
bot = telebot.TeleBot(token_in)
f.close()

f2 = open(r"C:\Users\Anton\PycharmProjects\Python-tel-bot\data\answer", "r")
hi_answer = ["Привет!",
            "Hi, amigos!",
            "Ола,сеньерэ",
            "🤝",
            "✌🏻",
            "👋🏻",
            "🤪",
            "Я ждал тебя!!",
            "Ок,приступим к продаже гаража!",
            "Я знал, что ты придешь!",
            "Ты опоздал, мир захвачен!",
            "Если ты наделяешь себя властью забирать жизни, жаждой власти и владением другими, то у тебя нет ничего.",
            "Всё кончено, ...! Я стою выше тебя!",
            "Полёты — это для дроидов.",
            "Всем доброго FPS'а!",
            "Бонд. Джеймс Бонд."]
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
def get_course_valute(name_valute):
    try:
        name = data['Valute'][name_valute]['Name']
        value = data['Valute'][name_valute]['Value']
        nominal = data['Valute'][name_valute]['Nominal']
        print(data['Valute'][name_valute]['Name'])
        return name, value, nominal
    except Exception as ex:
        print(ex)


def main():
    name_valute = "USD"
    get_course_valute(name_valute)

if __name__=='__main__':
    main()






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
        bot.send_message(message.chat.id, text=random.choice(hi_answer))
    elif (message.text == "👼🏼 Выберите действие"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👀 Проверить курс валюты")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1)
        markup.add(back)
        bot.send_message(message.chat.id, text="👼🏼 Выберите действие", reply_markup=markup)

    elif (message.text == "👀 Проверить курс валюты"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Доллар США")             # USD
            button2 = types.KeyboardButton("Евро")                   # EUR
            button3 = types.KeyboardButton("Дирхам ОАЭ")             # AED
            button4 = types.KeyboardButton("Австралийский доллар")   # AUD
            button5 = types.KeyboardButton("Болгарский лев")         # BGN
            button6 = types.KeyboardButton("Бразильский реал")       # BRL
            button7 = types.KeyboardButton("Белорусский рубль")      # BYN
            button8 = types.KeyboardButton("Канадский доллар")       # CAD
            button9 = types.KeyboardButton("Швейцарский франк")      # CHF
            button10 = types.KeyboardButton("Китайский юань")        # CNY
            button11 = types.KeyboardButton("Датская крона")         # DKK
            button12 = types.KeyboardButton("Японских иен")          # JPY
            back2 = types.KeyboardButton("Вернуться в главное меню")
            markup.add(button1, button2, button3)
            markup.add(button4, button5, button6)
            markup.add(button7, button8, button9)
            markup.add(button10, button11, button12)
            markup.add(back2)
            bot.send_message(message.chat.id, text="👀 Проверить курс валюты", reply_markup=markup)


    elif (message.text == "Доллар США"):
        name_valute = "USD"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")

    elif (message.text == "Евро"):
        name_valute = "EUR"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")

    elif (message.text == "Дирхам ОАЭ"):
        name_valute = "AED"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")

    elif (message.text == "Австралийский доллар"):
        name_valute = "AUD"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")

    elif (message.text == "Болгарский лев"):
        name_valute = "BGN"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")

    elif (message.text == "Бразильский реал"):
        name_valute = "BRL"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")

    elif (message.text == "Белорусский рубль"):
        name_valute = "BYN"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")

    elif (message.text == "Канадский доллар"):
        name_valute = "CAD"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")

    elif (message.text == "Швейцарский франк"):
        name_valute = "CHF"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")

    elif (message.text == "Китайский юань"):
        name_valute = "CNY"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")

    elif (message.text == "Датская крона"):
        name_valute = "DKK"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")

    elif (message.text == "Японских иен"):
        name_valute = "JPY"
        name, value, nominal = get_course_valute(name_valute)
        bot.send_message(message.chat.id, f"{nominal} {name} сейчас стоит {value} рублей")


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("👼🏼 Выберите действие")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)
