import telebot
from telebot import types

bot = telebot.TeleBot('6391904653:AAFUXq4NfZX8VeFR3tRj7KQ8F-c_aeSLT4s')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Расписание")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Расписание':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('5А')
        btn2 = types.KeyboardButton('5Б')
        btn3 = types.KeyboardButton('5В')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Выберете класс', reply_markup=markup) #ответ бота
    if message.text == '5А':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Понедельник')
        btn2 = types.KeyboardButton('Вторник')
        btn3 = types.KeyboardButton('Среда')
        btn4 = types.KeyboardButton('Четверг')
        btn5 = types.KeyboardButton('Пятница')
        btn6 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, 'Выберете день недели', reply_markup=markup) #ответ бота
    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('5А')
        btn2 = types.KeyboardButton('5Б')
        btn3 = types.KeyboardButton('5В')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Выберете класс', reply_markup=markup)

    elif message.text == 'Понедельник':
        bot.send_message(message.from_user.id,"""Понедельник: 
     1.Разговоры о важном 
     2.Английский язык 
     3.Русский язык 
     4.Биология 
     5.Математика""", parse_mode='Markdown')

    elif message.text == 'Вторник':
        bot.send_message(message.from_user.id, """
     1.Функциональная грамотность
     2.Математика
     3.Русский язык
     4.Литература
     5.Рисование""", parse_mode='Markdown')

    elif message.text == 'Среда':
        bot.send_message(message.from_user.id, """
     1.Рассказы по истории Отечества
     2.Мастерская творчества
     3.Английский язык
     4.Русский язык
     5.Физкультура
     6.Литература""", parse_mode='Markdown')
    elif message.text == 'Четверг':
        bot.send_message(message.from_user.id, """
     1.Математика
     2.Физкультура
     3.Технология
     4.Технология
     5.История""", parse_mode='Markdown')
    elif message.text == 'Пятница':
        bot.send_message(message.from_user.id, """
     1.Математика
     2.Русский язык
     3.ОДНКР
     4.Литература
     5.История""", parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)