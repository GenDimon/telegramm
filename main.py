from extrnsion import Parse, APIExeprion
import asyncio
from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
import os

load_dotenv()
bot = AsyncTeleBot(os.getenv('TOCKEN'))


@bot.message_handler(commands=['help', 'start'])
async def start(message):
    await bot.reply_to(message,
                       'Вы должны написать сообщение в котором будет написано: <название валюты цену которой вы хотите узнать> <название валюты в которой надо узнать цену> <количество первой валюты (если не укажете будет посчитана 1)>\nПример:\nRUB EUR 100\nЧтобы увидеть все поддериживаемые валюты введите /values')


@bot.message_handler(commands=['values'])
async def start(message):
    await bot.reply_to(message, f'Все поддерживаемые валюты: {Parse.get_all_val()}')

@bot.message_handler(content_types=['text'])
async def get(message):
    message_text = message.text.split()
    if len(message_text) == 3:
        answer = Parse.get_prise(message_text[0].upper(), message_text[1].upper(), message_text[2])
    elif len(message_text) == 2:
        answer = Parse.get_prise(message_text[0].upper(), message_text[1].upper())
    else:
        answer = APIExeprion('Вы не правильно ввели сообщение, вызовите функцию /help для более подробного объяснения ввода')

    await bot.reply_to(message, answer)

asyncio.run(bot.polling())