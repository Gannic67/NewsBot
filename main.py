import telebot
from baza import smol
from baza import getmoscow
from baza import get
from baza import smols
from config import TOKEN


bot = telebot.TeleBot(TOKEN)

# news1 = {
#     'smolensk': {
#         'news1': {
#             'description': 'Ремонт дорог'
#         },
#         'news2': {
#                  'description': 'Дтп'
#                  },
#         'poster': {
#                     'Entertainment': 'Кино-Афиша'
#                     }
#     },
#     'moscow': {
#         'news1': {
#             'description': 'Погода'
#         },
#         'news2': {
#             'description': 'Новости города'
#         }
#     }
# }




@bot.message_handler(commands=['start'])
def welcome(message):
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
    news = get()
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
    news = getmoscow()
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
    news = smols()
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = telebot.types.KeyboardButton("Вернуться в меню")
    keyboard.add(back)
    for i in news:
        message_list = []
        message_list.append({"pressed_count": 1})
        bot.send_message(chat_id, i, reply_markup=keyboard)



@bot.message_handler(func=lambda message: message.text == 'Вернуться в меню')
def back_to_menu(message):
    welcome(message)






if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()

