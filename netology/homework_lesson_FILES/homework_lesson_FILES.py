from pprint import pprint


def cook_book_interpritator(recipes_file):
    with open(recipes_file, encoding="utf-8") as file:

        book = {}

        for line in file:
            dish = line.strip()
            quantity = file.readline().strip()
            recipe = []

            for ingredients in range(int(quantity)):
                text = file.readline().split(" | ")
                recipe.append(
                    {'ingredient_name': text[0], 'quantity': int(text[1]),
                     'measure': text[2].strip()})
            book[dish] = recipe
            file.readline()
    return book


cook_book = cook_book_interpritator("recipes.txt")


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient["ingredient_name"] not in result:
                    result[ingredient["ingredient_name"]] = {
                        'measure': ingredient["measure"],
                        'quantity': ingredient['quantity'] * person_count}
                else:
                    result[ingredient["ingredient_name"]]['quantity'] = \
                    result[ingredient["ingredient_name"]]['quantity'] + \
                    ingredient['quantity'] * person_count
        else:
            print(f"\nБлюда {dish} нет в книге рецептов.\n")
    return result


pprint(get_shop_list_by_dishes(['Омлет', 'Глазунья', 'Торт'], 3))
