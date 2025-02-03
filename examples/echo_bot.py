#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

API_TOKEN = '<7255443982:AAG_XZc4SLXqD9x8cTf8l3GT5ybcje0QnwY>'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(ciao):
    bot.reply_to(naia, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
if message.text=='Ciao':
        bot.reply_to(message, 'Ciao io sono un gay, come stai?')
elif message.text=='Bene':
    bot.reply_to(message, 'Bene anchio sono gay')
else: 
 bot.reply_to(message, 'Sono gay, non capisco')


bot.infinity_polling()
