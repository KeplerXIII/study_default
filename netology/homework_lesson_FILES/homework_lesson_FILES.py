from pprint import pprint


def cook_book_generator(recipes_file):
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
    temp = [file1, file2, file3]
    text_list = []
    for file in temp:
        with open(file, encoding="utf-8") as f:
            f_list = f.readlines()
            f_len = str(len(f_list))
            f_list.insert(0, f_len + "\n")
            f_list.insert(0, file + "\n")
            text_list.append(f_list)
    text_list.sort(key=len)
    with open("4.txt", "w", encoding='utf-8') as file_4:
        file_4.write("".join(text_list[0]) + "\n" + "".join(text_list[1]) + "\n" + "".join(text_list[2]))


cook_book = cook_book_generator("recipes.txt")
pprint(get_shop_list_by_dishes(['Омлет', 'Глазунья', 'Торт'], 3))
text_combiner("3.txt", "1.txt", "2.txt")
