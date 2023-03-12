import telebot
import os
from random import choice

from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def strat(message):
    mess = (f'Привет, <b>{message.from_user.first_name}</b>! '
            f'Я Магический Бот Восьмёрка. '
            f'Задай мне вопрос и мы вместе посмотриим в будущее!')
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if '?' in message.text.lower():
        sticker = open('answers/' + choice(os.listdir('answers')), 'rb')
        bot.send_sticker(message.chat.id, sticker)
    else:
        bot.send_message(message.chat.id,
                         f'<b>{message.from_user.first_name}</b>, '
                         f'это не вопрос!',
                         parse_mode='html')


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
