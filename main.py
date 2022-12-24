import telebot

import count_rating
import decoding
import encoding
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(msg):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    key_encod = telebot.types.KeyboardButton('Кодировать')
    key_decod = telebot.types.KeyboardButton('Декодировать')

    markup.add(key_encod, key_decod)
    bot.send_message(msg.chat.id, 'пожелания', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(msg):
    if msg.text == 'Кодировать':
        bot.send_message(msg.chat.id, 'Введите текст для кодирования: ')
        bot.register_next_step_handler(msg, encod_text)

    elif msg.text == 'Декодировать':
        bot.send_message(msg.chat.id, 'Введите текст для декодирования:  ')
        bot.register_next_step_handler(msg, decod_text)


@bot.callback_query_handler(
    func=lambda call: call.data.startswith('like'))  # ценка лайк -> ведётся подсчёт в отдельном файле
def callback_handler(call):
    count_rating.like()
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, 'Спасибо за вашу оценку')


@bot.callback_query_handler(
    func=lambda call: call.data.startswith('Dislike'))  # ценка лайк -> ведётся подсчёт в отдельном файле
def callback_handler(call):
    count_rating.dislike()
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, 'Спасибо за вашу оценку!')


@bot.message_handler(content_types=['text'])
def encod_text(messeg):
    bot.send_message(messeg.chat.id, f'{encoding.encoding(messeg.text)}')
    markup_inline = telebot.types.InlineKeyboardMarkup()
    key_rating_like = telebot.types.InlineKeyboardButton(text='Понравилось', callback_data='like')
    key_rating_dislike = telebot.types.InlineKeyboardButton(text='Не понравилось', callback_data='Dislike')
    markup_inline.add(key_rating_like, key_rating_dislike)
    bot.send_message(messeg.chat.id, 'Оцени меня!', reply_markup=markup_inline)


@bot.message_handler(content_types=['text'])
def decod_text(messeg):
    bot.send_message(messeg.chat.id, f'{decoding.decoding(messeg.text)}')
    markup_inline = telebot.types.InlineKeyboardMarkup()
    key_rating_like = telebot.types.InlineKeyboardButton(text='Понравилось', callback_data='like')
    key_rating_dislike = telebot.types.InlineKeyboardButton(text='Не понравилось', callback_data='Dislike')
    markup_inline.add(key_rating_like, key_rating_dislike)
    bot.send_message(messeg.chat.id, 'Оцени меня!', reply_markup=markup_inline)


bot.polling(none_stop=True)
