def task1():

    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

    while True:
        boys.sort()
        girls.sort()
        if len(boys) == len(girls):
            zipped_pairs = zip(boys, girls)

            print("Идеальные пары: ")
            for boys, girls in zipped_pairs:
                print(f'{boys} и {girls}')
            break
        else:
            if len(boys) > len(girls):
                print(f'Что бы шансы были равны, нужно добавть женских анкет: {len(boys) - len(girls)} шт.')
                girl_profile = input("Введите имя анкеты: ")
                girls.append(girl_profile)

            else:
                print(f'Что бы шансы были равны, нужно добавть мужских анкет: {len(girls) - len(boys)} шт')
                boy_profile = input("Введите имя анкеты: ")
                boys.append(boy_profile)

def task2():
    cook_book = [
        ['салат',
         [
             ['картофель', 100, 'гр.'],
             ['морковь', 50, 'гр.'],
             ['огурцы', 50, 'гр.'],
             ['горошек', 30, 'гр.'],
             ['майонез', 70, 'мл.'],
         ]
         ],
        ['пицца',
         [
             ['сыр', 50, 'гр.'],
             ['томаты', 50, 'гр.'],
             ['тесто', 100, 'гр.'],
             ['бекон', 30, 'гр.'],
             ['колбаса', 30, 'гр.'],
             ['грибы', 20, 'гр.'],
         ],
         ],
        ['фруктовый десерт',
         [
             ['хурма', 60, 'гр.'],
             ['киви', 60, 'гр.'],
             ['творог', 60, 'гр.'],
             ['сахар', 10, 'гр.'],
             ['мед', 50, 'мл.'],
         ]
         ]
    ]
    person = int(input("Введите количество персон: "))

    for dish, ingredients in cook_book:
        print(f'{dish.capitalize()}:')
        for ingredient, weight, count in ingredients:
            print(f'{ingredient}, {weight * person}{count}')
        print()
