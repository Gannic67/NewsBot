import telebot

from baza import smol
from baza import get
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

news = {
    'smolensk': {
        'news1': {
            'description': 'Ремонт дорог'
        },
        'news2': {
                 'description': 'Дтп'
                 },
        'poster': {
                    'Entertainment': 'Кино-Афиша'
                    }
    },
    'moscow': {
        'news1': {
            'description': 'Погода'
        },
        'news2': {
            'description': 'Новости города'
        }
    }
}




@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton("Новости Смоленск")
    button2 = telebot.types.KeyboardButton("Новости Москва")
    keyboard.add(button2, button1)
    bot.send_message(chat_id, 'Привет!Спасибо, что читаешь новости ', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Новости Москва')
def moscow(message):
    news = get()
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button2 = telebot.types.KeyboardButton("Новости города")
    back = telebot.types.KeyboardButton("Вернуться в меню")
    keyboard.add(button2)
    keyboard.add(back)
    bot.send_message(chat_id, news, reply_markup=keyboard)



@bot.message_handler(func=lambda message: message.text == 'Новости Смоленск')
def smolensk(message):
    new = smol()
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton("Общие новости")
    back = telebot.types.KeyboardButton("Вернуться в меню")
    keyboard.add(button1, back)
    bot.send_message(chat_id, new, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Вернуться в меню')
def back_to_menu(message):
    welcome(message)




if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()

