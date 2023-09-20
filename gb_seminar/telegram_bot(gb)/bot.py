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

    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton("/Random_film")
    button2 = types.KeyboardButton("/Random_book")
    button3 = types.KeyboardButton("/All books and films")
    button4 = types.KeyboardButton("/help")

    keyboard.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, "I'm - <b>{1.first_name}</b>, puppet-bot.".format(
        message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def process_help_command(message):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        commands = data['commands']
    bot.send_message(message.chat.id, '\n'.join(commands))


@bot.message_handler(commands=['Random_film'])
def process_random_film_command(message):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        movies = data['movies']
    bot.send_message(message.chat.id, str(choice(movies)))


@bot.message_handler(commands=['Random_book'])
def process_random_book_command(message):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        books = data['books']
    bot.send_message(message.chat.id, str(choice(books)))


@bot.message_handler(commands=['All_books_and_films'])
def process_all_books_and_films_command(message):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        books = data['books']
        movies = data['movies']
        heading_books = "Books📖:\n"
        heading_movies = "Movies🎬:\n"
        result_books = heading_books + '\n'.join(books)
        result_movies = heading_movies + '\n'.join(movies)

    bot.send_message(message.chat.id, '\n' + result_books + '\n' + result_movies)


@bot.message_handler(commands=['add_film'])
def process_add_film_command(message):
    bot.send_message(message.chat.id, 'Input title of film 🎬')
    bot.register_next_step_handler(message, process_add_film)


@bot.message_handler(commands=['add_book'])
def process_add_book_command(message):
    bot.send_message(message.chat.id, 'Type  a title of book 📖')
    bot.register_next_step_handler(message, process_add_book)


@bot.message_handler(commands=['delete_film'])
def process_delete_film_command(message):
    bot.send_message(message.chat.id, 'Input name of erased film 🎬')
    bot.register_next_step_handler(message, process_delete_film)


@bot.message_handler(commands=['delete_book'])
def process_delete_book_command(message):
    bot.send_message(message.chat.id, 'Input name of erased book 📖')
    bot.register_next_step_handler(message, process_delete_book)


@bot.message_handler(commands=['show_movies'])
def process_show_movies_command(message):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        movies = data['movies']
        heading_movies = "Movies🎬:\n"
        result_movies = heading_movies + '\n'.join(movies)
    bot.send_message(message.chat.id, '\n' + result_movies)


@bot.message_handler(commands=['show_books'])
def process_show_books_command(message):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        movies = data['books']
        heading_books = "Books📖:\n"
        result_books = heading_books + '\n'.join(movies)
    bot.send_message(message.chat.id, '\n' + result_books)


@bot.message_handler(content_types=['text'])
def chatting(message):
    if message.chat.type == 'private':

        if message.text == 'start':
            bot.send_message(message.chat.id, 'Bot film-keeper begins to work')
        else:
            bot.send_message(message.chat.id, "I don't understand you")
