from pprint import pprint

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

shelf_range = list(directories.keys())
error_message = "Такого номера нет в списке документов."
shelf_error = f"Полки не существует, для добавления доступны {shelf_range}"
profile_error = "Профайл не найден"

greeting = '''
Добро пожаловть в doc_controller, с помощью этой программы вы можете добавлять документы в базу, 
сортировать их по полкам, а так же перемещать их. Для начала работы ознакомьтесь с возможностями.
'''

commands = '''
p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит.
s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится.
a – add – команда, которая добавит новый документ в каталог и в перечень полок.
m - move - перемещает указанный документ на указанную полку.
l – list – команда, которая выведет список всех документов.
h - help - выводит список команд.
q - quit - выйти из программы.
d - delete - удаляет документ.
as – add shelf – добавляем новую полку.
'''


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap


@decor
def name_search():
    number = input("Введите номер документа для поиска имени: ")
    for profile in documents:
        if profile["number"] == number:
            print(f'По запрошенному номеру документа в базе найден:{profile["name"]}')
            return
    print(error_message)


@decor
def shelf_search():
    number = input("Введите номер документа для поиска полки: ")
    for shelf in directories:
        if number in directories[shelf]:
            print(f'Документ на полке: {shelf}')
            return
    print(error_message)


@decor
def list_documents():
    for profile in documents:
        print(f"{profile['type']}, {profile['number']}, {profile['name']}")


@decor
def add_profile():
    shelf = input("Введите номер полки для хранения: ")
    if shelf not in list(directories.keys()):
        print(shelf_error)
        return
    number = input("Введите номер документа для добавления: ")
    type = input("Введите тип документа: ")
    name = input("Введите имя: ")
    documents.append({'type': type, 'number': number, 'name': name})
    directories[shelf] += [number]
    print(f"Документ добавлен на {shelf} полку.")


@decor
def delete():
    number = input("Введите номер документа для удаления: ")
    for profile in documents:
        if profile['number'] == number:
            documents.remove(profile)
    for shelf in directories:
        if number in directories[shelf]:
            directories[shelf].remove(number)
            print("Профайл удалён.")
            return
    print(profile_error)


@decor
def move():
    number = input("Введите номер документа для перемещения: ")
    finish_shelf = input("Введите номер полки для перемещения: ")
    if finish_shelf not in list(directories.keys()):
        return shelf_error
    for shelf in directories:
        if number in directories[shelf]:
            directories[shelf].remove(number)
            directories[finish_shelf] += [number]
            print(f"Документ перемещен на полку {finish_shelf}")
            return
    print(f'Профайл не найден')


@decor
def add_shelf():
    number = input("Введите номер полки для добавления: ")
    if number not in list(directories.keys()):
        directories[number] = []
        print(f'Полка {number} добавлена.')
        return
    print(f'Полка {number} уже существует.')


@decor
def check():
    pprint(documents)
    pprint(directories)


@decor
def help():
    print(commands)


commands_dict = {
    "p": name_search,
    "s": shelf_search,
    'l': list_documents,
    'a': add_profile,
    'd': delete,
    'm': move,
    'h': help,
    'as': add_shelf,
    'check': check
}


def doc_controller():
    print(greeting)
    print(commands)
    while True:
        command = input("Введите команду: ").lower()
        if command in list(commands_dict.keys()):
            commands_dict[command]()
        elif command == "q":
            print("Работа завершена. Спасибо за использование doc_controller.")
            return
        else:
            print("Введена недопустимая команда, повторите ввод.")


doc_controller()