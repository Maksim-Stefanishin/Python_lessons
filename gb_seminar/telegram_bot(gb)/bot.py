import config
import json
from random import *
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


def process_add_film(message):
    with open("data.json", "r") as file:
        data = json.load(file)
        if message.text in data['movies']:
            bot.send_message(message.chat.id, 'This film is already in the list . Try another')


        else:
            data['movies'].append(message.text)
            with open("data.json", "w") as file:
                json.dump(data, file, ensure_ascii=False)
            bot.send_message(message.chat.id, 'Film was added')


def process_add_book(message):
    with open("data.json", "r") as file:
        data = json.load(file)
        if message.text in data['books']:
            bot.send_message(message.chat.id, 'This book is already in the list . Try another')
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, ensure_ascii=False)
            bot.send_message(message.chat.id, 'Book was added')


def process_delete_film(message):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        data['movies'].remove(message.text)
        with open("data.json", "w", ) as file:
            json.dump(data, file, ensure_ascii=False)

        bot.send_message(message.chat.id, 'Film was erased')
    except:
        bot.send_message(message.chat.id, 'Oops. there is no such film. Try another')


def process_delete_book(message):
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        data['books'].remove(message.text)
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

        bot.send_message(message.chat.id, 'Book was deleted')
    except:
        bot.send_message(message.chat.id, 'Oops. there is no such book. Try another')


@bot.message_handler(commands=['start'])
def process_start_command(message):
    sti = open('files/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button1 = types.KeyboardButton("🎬 Random film ")
    button2 = types.KeyboardButton("📖 Random book")
    button3 = types.KeyboardButton("📖/🎬 All books and films")
    button4 = types.KeyboardButton("Help")

    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, "I'm - <b>{1.first_name}</b>, puppet-bot.".format(
        message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def chatting(message):
    if message.chat.type == 'private':

        if message.text == 'start':
            bot.send_message(message.chat.id, 'Bot film-keeper begins to work')

        elif message.text == '📖/🎬 All books and films':
            with open('data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                books = data['books']
                movies = data['movies']
                heading_books = "Books📖:\n"
                heading_movies = "Movies🎬:\n"
                result_books = heading_books + '\n'.join(books)
                result_movies = heading_movies + '\n'.join(movies)

            bot.send_message(message.chat.id, '\n' + result_books + '\n' + result_movies)
        elif message.text == '🎬 Random film':
            with open('data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                movies = data['movies']
            bot.send_message(message.chat.id, str(choice(movies)))
        elif message.text == '📖 Random book':
            with open('data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                books = data['books']
            bot.send_message(message.chat.id, str(choice(books)))
        elif message.text == 'add film':
            bot.send_message(message.chat.id, 'Input title of film 🎬')
            bot.register_next_step_handler(message, process_add_film)
        elif message.text == 'add book':
            bot.send_message(message.chat.id, 'Type  a title of book 📖')
            bot.register_next_step_handler(message, process_add_book)
        elif message.text == 'delete film':
            bot.send_message(message.chat.id, 'Input name of erased film 🎬')
            bot.register_next_step_handler(message, process_delete_film)
        elif message.text == 'delete book':
            bot.send_message(message.chat.id, 'Input name of erased book 📖')
            bot.register_next_step_handler(message, process_delete_book)
        elif message.text == 'Help':
            with open('data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                commands = data['commands']
            bot.send_message(message.chat.id, '\n'.join(commands))
        elif message.text == 'show movies':
            with open('data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                movies = data['movies']
                heading_movies = "Movies🎬:\n"
                result_movies = heading_movies + '\n'.join(movies)
            bot.send_message(message.chat.id, '\n' + result_movies)
        elif message.text == 'show books':
            with open('data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                movies = data['books']
                heading_books = "Books📖:\n"
                result_books = heading_books + '\n'.join(movies)
            bot.send_message(message.chat.id, '\n' + result_books)
        else:
            bot.send_message(message.chat.id, "Don't know how to answer 😢")


bot.infinity_polling(skip_pending=True)
