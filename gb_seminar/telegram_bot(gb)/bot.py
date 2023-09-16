import config
import json
from random import *

import telebot
from telebot import types

global items

bot = telebot.TeleBot(config.TOKEN)

films = ['Matrix', "Solaris", "Lord of the Rings", 'Dunkirk']
data = []


def process_add(message):
    with open("films.json", "r") as file:
        films = json.load(file)
    films.append(message.text)
    with open("films.json", "w", ) as file:
        json.dump(films, file, ensure_ascii=False)
    print(films)

    bot.send_message(message.chat.id, 'Film added')


def process_delete(message):
    try:
        with open("films.json", "r") as file:
            films = json.load(file)
        films.remove(message.text)
        with open("films.json", "w", ) as file:
            json.dump(films, file, ensure_ascii=False)

        bot.send_message(message.chat.id, 'Film deleted')
    except:
        bot.send_message(message.chat.id, 'Oops. there is no such film. Try another')


# @bot.message_handler(commands=['start'])
# def welcome(message):
#     # sti = open('static/sticker.webp', 'rb')
#     # bot.send_sticker(message.chat.id, sti)
#
#     # keyboard
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
#     item1 = types.KeyboardButton("🎲 Рандомное число")
#     item2 = types.KeyboardButton("😊 Как дела?")
#
#     markup.add(item1, item2)
#
#     bot.reply_to(message.chat.id, "Я - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(
#         message.from_user, bot.get_me()),
#                  parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def film_list(message):

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")

    markup.add(item1, item2)
    if message.chat.type == 'private':

        if message.text == 'start':
            bot.send_message(message.chat.id, 'Bot film-keeper begins to work')

        elif message.text == 'all':
            with open('films.json', 'r') as file:
                films = json.load(file)
            bot.send_message(message.chat.id, str(films))
        elif message.text == 'random':
            with open("films.json", "r") as file:
                films = json.load(file)
            bot.send_message(message.chat.id, str(choice(films)))
        elif message.text == 'add':
            bot.send_message(message.chat.id, 'Input added film')
            bot.register_next_step_handler(message, process_add)
        elif message.text == 'delete':
            bot.send_message(message.chat.id, 'Input name of erased film')
            bot.register_next_step_handler(message, process_delete)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


# def save():
#     with open('films.json', 'w', encoding='utf-8') as file:
#         json.dump(films, file, ensure_ascii=False)
#     print('Our film-library was successfully saved in films.json')
#     print(films)
#
#
# def load():
#     with open('films.json', 'r', encoding='utf-8') as file:
#         print('Film list was successfully loaded')
#         films = json.load(file)
#         print(films)
#         return films
#
#
# while True:
#
#     command = input('Input command: ')
#
#     if command == 'start':
#         print('Bot film-keeper begins to work')
#
#     elif command == 'stop':
#         save()
#         print('Bot end his work. Try again soon.')
#         break
#
#     elif command == 'all':
#         with open("films.json", "r") as file:
#             print('This is actual films list')
#             films = json.load(file)
#             print(films)
#
#     elif command == 'add':
#         with open("films.json", "r") as file:
#             films = json.load(file)
#             f = input('Input name of film: ')
#             films.append(f)
#         with open("films.json", "w") as file:
#             json.dump(films, file)
#
#         print('Film was successfully added')
#
#     elif command == 'help':
#         print('Here should be a link to manual')
#
#     elif command == 'delete':
#         try:
#
#             with open("films.json", "r") as file:
#                 films = json.load(file)
#                 f = input('Input name of film to remove: ')
#                 films.remove(f)
#             with open("films.json", "w") as file:
#                 json.dump(films, file)
#             print('Film was successfully removed')
#         except:
#             print('Oops. there is no such film. Try another')
#
#     elif command == 'random':
#         with open("films.json", "r") as file:
#             films = json.load(file)
#
#             print('Random film from list is ' + choice(films))
#     elif command == 'save':
#         save()
#
#     elif command == 'load':
#         load()
#
#     else:
#         print('Incorrect command. Please, read manual. use /help')

bot.infinity_polling(skip_pending=True)
