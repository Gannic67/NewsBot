import telebot
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
            'description': 'Благоустройство города'
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
    bot.send_message(chat_id,'Добро пожаловать!', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Новости Москва')
def smol(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton("Погода")
    button2 = telebot.types.KeyboardButton("Благоустройство города")
    keyboard.add(button1, button2)
    bot.send_message(chat_id, 'Выбирите пункт', reply_markup=keyboard)



@bot.message_handler(func=lambda message: message.text == 'Новости Смоленск')
def moscow(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton("Ремонт дорог")
    button2 = telebot.types.KeyboardButton("Дтп")
    button3 = telebot.types.KeyboardButton("Кино-Афиша")
    keyboard.add(button1, button2)
    keyboard.add(button3)
    bot.send_message(chat_id,'Выбирите пункт', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Вернуться в главное меню')
def exit(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = telebot.types.KeyboardButton("Вернуться в главное меню")
    keyboard.add(back)
    bot.send_message(chat_id, 'Выбирите пункт', reply_markup=keyboard)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()

