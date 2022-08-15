from pprint import pprint

def cook_book():
    with open("recipes.txt", encoding="utf-8") as file:
        cook_book = {}

        for line in file:
            dish = line.strip()
            quantity = file.readline().strip()
            recipe = []

            for line in range(int(quantity)):
                text = file.readline().split(" | ")
                recipe.append({'ingredient_name': text[0], 'quantity': text[1],
                               'measure': text[2].strip()})
            cook_book[dish] = recipe
            file.readline()
    return cook_book


cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            result[ingredient["ingredient_name"]] = {'measure': ingredient["measure"], 'quantity': ingredient['quantity'] * person_count}
        return result




pprint(get_shop_list_by_dishes(["Омлет"], 3))

