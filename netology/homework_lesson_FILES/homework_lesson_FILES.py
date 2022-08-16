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
            print(f"\nБлюда '{dish}' нет в книге рецептов.\n")
    return result


def text_combiner(file1, file2, file3):
    with open(file1, encoding='utf-8') as file_1:
        text1_list = file_1.readlines()
        text1_len = str(len(text1_list))
        text1_list.insert(0, text1_len + "\n")
        text1_list.insert(0, file1 + '\n')

    with open(file2, encoding='utf-8') as file_2:
        text2_list = file_2.readlines()
        text2_len = str(len(text2_list))
        text2_list.insert(0, text2_len + "\n")
        text2_list.insert(0, file2 + '\n')

    with open(file3, encoding='utf-8') as file_3:
        text3_list = file_3.readlines()
        text3_len = str(len(text3_list))
        text3_list.insert(0, text3_len + "\n")
        text3_list.insert(0, file3 + '\n')

    sort_list = [text1_list, text2_list, text3_list]
    sort_list.sort(key=len)

    with open("4.txt", "w", encoding='utf-8') as file_4:
        file_4.write(
            "".join(sort_list[0]) + "\n" + "".join(sort_list[1]) + "\n" + "".join(sort_list[2]))


cook_book = cook_book_interpritator("recipes.txt")
pprint(get_shop_list_by_dishes(['Омлет', 'Глазунья', 'Торт'], 3))
text_combiner("3.txt", "1.txt", "2.txt")
