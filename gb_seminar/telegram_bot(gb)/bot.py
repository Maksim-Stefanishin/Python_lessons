from random import *
import json

films = ['Matrix', "Solaris", "Lord of the Rings", 'Dunkirk', 'Pregnant in 16th']


def save():
    with open('films.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    print('Our film-library was successfully saved in film.json')


def load():
    with open('films.json', 'r', encoding='utf-8') as fh:
        films = json.load(fh)
    print('Film list was successfully loaded')


try:
    load()
except:
    films = ['Matrix', "Solaris", "Lord of the Rings", 'Dunkirk', 'Pregnant in 16th']

# def load():
#     with open('films.json', 'r', encoding='utf-8') as fh:
#         films = json.load(fh)
#     print('Film list successfully load')


while True:
    command = input('Input command: ')
    if command == 'start':
        print('Bot film-keeper begins work')
    elif command == 'stop':
        save()
        print('Bot end his work. Try again soon.')
        break
    elif command == 'print_all':
        print('This is actual films list')
        print(films)
    elif command == 'add':
        f = input('Input name of film: ')
        films.append(f)
        print('Film was successfully added')
    elif command == 'help':
        print('Here should be a link to manual')
    elif command == 'delete':
        f = input('Input name of film to remove: ')

        '''
        if f not in films:
            print('Oops. there is no such film. Try another')
        
        else:
            print('Film was erased from list')
            films.remove(f)
        '''
        try:
            films.remove(f)
            print('Film was erased from list')
        except:
            print('Oops. there is no such film. Try another')
    elif command == 'random':
        # rnd = randint(0, len(films)-1)
        # print('Random film from list is '+films[rnd])
        print('Random film from list is ' + choice(films))
    elif command == 'save':
        save()

    elif command == 'load':
        load()
        print(films)
        '''
        with open('films.json', 'r', encoding='utf-8') as fh:
            films = json.load(fh)
        print('Film list successfully load')
        '''
    else:
        print('Incorrect command. Please, read manual. use /help')
