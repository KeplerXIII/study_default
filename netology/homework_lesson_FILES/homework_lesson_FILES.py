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

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient["ingredient_name"] not in result:
                    result[ingredient["ingredient_name"]] = {'measure': ingredient["measure"], 'quantity': ingredient['quantity'] * person_count}
                else:
                    result[ingredient["ingredient_name"]]['quantity'] = result[ingredient["ingredient_name"]]['quantity'] + ingredient['quantity'] * person_count
        else:
            print(f"Блюда {dish} нет в книге рецептов.")
    return result


pprint(get_shop_list_by_dishes(['Омлет', 'Глазунья', 'Торт'], 3))

