"""
Основной модуль бота в котором описана логика работы бота.
Взаимодействие его с базой данных посредством нажатия на кнопки
"""

import telebot
from baza import smol
from baza import news_moscow
from baza import moscow_generalnews
from baza import smol_news
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    """
    В этой функции мы сделали команду старт и приветствие пользователей.
    Далее создали кнопки, которая в аргументах содержит текст, отображаемый на кнопке.
    """
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton("Общие новости Смоленск")
    button2 = telebot.types.KeyboardButton('Происшествия Смоленск')
    button3 = telebot.types.KeyboardButton("Общие новости Москва")
    button4 = telebot.types.KeyboardButton('Происшествия Москва')
    keyboard.add(button1, button2)
    keyboard.add(button3, button4)

    bot.send_message(chat_id, 'Привет!Спасибо, что читаешь новости ', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Общие новости Москва')
def moscow(message):
    """
    Функция отвечающая за кнопку общие новости города Москва.С помощью цикла проходимся по таблице из базы данный MySql.
    Используем пустой список для хранения данных.
    Метод append используем для добавления элементов в список.
    Метододом count Возвращаем количество раз, сколько указаный элемент появляется в списке
    """
    news = moscow_generalnews()
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = telebot.types.KeyboardButton("Вернуться в меню")
    keyboard.add(back)
    for i in news:
        message_list = []
        message_list.append({"pressed_count": 1})
        bot.send_message(chat_id, i, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Происшествия Москва')
def moscow(message):
    """
    Функция отвечающая за кнопку общие новости города Москва.С помощью цикла проходимся по таблице из базы данный MySql.
     Используем пустой список для хранения данных.
    Метод append используем для добавления элементов в список.
     Метододом count Возвращаем количество раз, сколько указаный элемент появляется в списке
    """
    news = news_moscow()
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = telebot.types.KeyboardButton("Вернуться в меню")
    keyboard.add(back)
    for i in news:
        message_list = []
        message_list.append({"pressed_count": 1})
        bot.send_message(chat_id, i, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Общие новости Смоленск')
def smolensk(message):
    """
    Функция отвечающая за кнопку общие новости города Москва.С помощью цикла проходимся по таблице из базы данный MySql.
    Используем пустой список для хранения данных.
    Метод append используем для добавления элементов в список.
    Метододом count Возвращаем количество раз, сколько указаный элемент появляется в списке
    """
    news = smol()
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = telebot.types.KeyboardButton("Вернуться в меню")
    keyboard.add(back)
    for i in news:
        message_list = []
        message_list.append({"pressed_count": 1})
        bot.send_message(chat_id, i, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Происшествия Смоленск')
def smolensk(message):
    """
    Функция отвечающая за кнопку общие новости города Москва.С помощью цикла проходимся по таблице из базы данный MySql.
    Используем пустой список для хранения данных.
    Метод append используем для добавления элементов в список.
    Метододом count Возвращаем количество раз, сколько указаный элемент появляется в списке
    """
    news = smol_news()
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = telebot.types.KeyboardButton("Вернуться в меню")
    keyboard.add(back)
    for i in news:
        message_list = []
        message_list.append({"pressed_count": 1})
        bot.send_message(chat_id, i, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Вернуться в меню')   #
def back_to_menu(message):
    """
    Функция возврата в меню выбора новостей
    """

    welcome(message)

    """
    Запуск бота
    """
if __name__ == '__main__':
    print('Бот запущен!')
    while True:
        try:
            bot.infinity_polling()
        except:
            pass