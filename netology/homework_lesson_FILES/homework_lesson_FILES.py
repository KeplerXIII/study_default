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
                recipe.append({'ingredient_name': text[0], 'quantity': int(text[1]),
                               'measure': text[2].strip()})
            cook_book[dish] = recipe
            file.readline()
    return cook_book


cook_book = cook_book()
pprint(cook_book)


test = {'Молоко': {'measure': 'мл', 'quantity': 300},
       'Помидор': {'measure': 'шт', 'quantity': 6},
       'Яйцо': {'measure': 'шт.', 'quantity': 6}}


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient["ingredient_name"] not in result:
                result[ingredient["ingredient_name"]] = {'measure': ingredient["measure"], 'quantity': ingredient['quantity'] * person_count}
            else:
                result[ingredient["ingredient_name"]]['quantity'] = result[ingredient["ingredient_name"]]['quantity'] + ingredient['quantity'] * person_count
    return result




pprint(get_shop_list_by_dishes(['Омлет', 'Глазунья'], 3))

