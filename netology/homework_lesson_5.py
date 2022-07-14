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


def name_search(number):
    for profile in documents:
        if profile["number"] == number:
            return f'По запрошенному номеру документа в базе найден:{profile["name"]}'
    return error_message


def shelf_search(number):
    for shelf in directories:
        if number in directories[shelf]:
            return f'Документ на полке: {shelf}'
    return error_message


def list_documents():
    for profile in documents:
        print(f"{profile['type']}, {profile['number']}, {profile['name']}")


def add_profile(shelf, number, type, name):
    if shelf not in list(directories.keys()):
        return shelf_error
    documents.append({'type': type, 'number': number, 'name': name})
    directories[shelf] += [number]
    return f"Документ добавлен на {shelf} полку."


def delete(number):
    for profile in documents:
        if profile['number'] == number:
            documents.remove(profile)
    for shelf in directories:
        if number in directories[shelf]:
            directories[shelf].remove(number)
            return "Профайл удалён."
    return profile_error


def move(number, finish_shelf):
    if finish_shelf not in list(directories.keys()):
        return shelf_error
    for shelf in directories:
        if number in directories[shelf]:
            directories[shelf].remove(number)
            directories[finish_shelf] += [number]
            return f"Документ перемещен на полку {finish_shelf}"
    return f'Профайл не найден'


def add_shelf(number):
    if number not in list(directories.keys()):
        directories[number] = []
        return f'Полка {number} добавлена.'
    return f'Полка {number} уже существует.'


def offset():
    print("----------------")


def doc_controller():
    print(commands)
    while True:
        command = input("Введите команду: ").lower()
        if command == 'p' or command == 'people':
            offset()
            number = input("Введите номер документа для поиска имени: ")
            print(name_search(number))
            offset()
        elif command == 's' or command == 'shelf':
            offset()
            number = input("Введите номер документа для поиска полки: ")
            print(shelf_search(number))
            offset()
        elif command == 'l' or command == 'list':
            offset()
            list_documents()
            offset()
        elif command == 'a' or command == 'add':
            offset()
            shelf = input("Введите номер полки для хранения: ")
            shelf_checker(shelf)
            number = input("Введите номер документа для добавления: ")
            type = input("Введите тип документа: ")
            name = input("Введите имя: ")
            print(add_profile(shelf, number, type, name))
            offset()
        elif command == 'h' or command == 'help':
            offset()
            print(commands)
            offset()
        elif command == 'd' or command == 'delete':
            offset()
            number = input("Введите номер документа для удаления: ")
            print(delete(number))
            offset()
        elif command == 'm' or command == 'move':
            offset()
            number = input("Введите номер документа для перемещения: ")
            finish_shelf = input("Введите номер полки для перемещения: ")
            print(move(number, finish_shelf))
            offset()
        elif command == 'as' or command == 'add shelf':
            offset()
            number = input("Введите номер полки для добавления: ")
            print(add_shelf(number))
            offset()
        elif command == "q" or command == 'quit':
            offset()
            print("Работа завершена. Спасибо за пользование doc_controller.")
            offset()
            return
        else:
            offset()
            print("Введена недопустимая команда, повторите ввод.")
            offset()


doc_controller()
