def list_tuple_set():
    # именованный срез
    my_list = [1, 2, 3, 4, 5, 6, 7]
    even = slice(1, None, 2)
    print(my_list[even])  # [2, 4, 6]

    text = "Hello Man"
    rev = slice(None, None, -1)
    print(text[rev])  # naM olleH

    # вставки вместо .insert и .append
    my_list = [1, 2, 3, 4, 5]
    my_list[5:] = [6]  # вставляем в конец — лучше использовать .append(6)
    print(my_list)  # [1, 2, 3, 4, 5, 6]
    my_list[0:0] = [0]  # вставляем в начало — лучше использовать .insert(0, 0)
    print(my_list)  # [0, 1, 2, 3, 4, 5, 6]
    my_list[3:3] = [25]  # вставляем между элементами — лучше использовать .insert(3, 25)
    print(my_list)  # [0, 1, 2, 25, 3, 4, 5, 6]

    # изменение количества
    my_list = [1, 2, 3, 4, 5]
    my_list[1:3] = [20, 30]
    print(my_list)  # [1, 20, 30, 4, 5]
    my_list[1:3] = [0]  # нет проблем заменить два элемента на один
    print(my_list)  # [1, 0, 4, 5]
    my_list[2:] = [40, 50, 60]  # или два элемента на три
    print(my_list)  # [1, 0, 40, 50, 60]

    # sorted() - создаёт новый список [], причем возможно применения ключей
    # .sort() - применим только к спискам
    my_files = ['somecat.jpg', 'pc.png', 'apple.bmp', 'mydog.gif']
    my_files_sorted = sorted(my_files, key=len)  # сортировка по длине
    print(my_files_sorted)  # ['pc.png', 'apple.bmp', 'mydog.gif', 'somecat.jpg']

    my_set = {2, 5, 1, 7, 3}
    my_set_sorted = sorted(my_set, reverse=True)
    print(my_set_sorted)  # [7, 5, 3, 2, 1]

    # Добавляем все элементы второго списка к элементам первого с измением первого списка методом .extend():
    # Объединение списков
    a = []
    b = []
    a.extend(b)    # a += b эквивалентно a.extend(b)
    print(a, b)    # [1, 2, 3, 4, 5]  [4, 5]

    # Добавление элемента
    a.append(b)  # a += [b] эквивалентно a.append(b)
    print(a, b)  # [1, 2, 3, [4, 5]]  [4, 5]

    # Добавление в словарь
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 100, 'c': 3, 'd': 4}
    dict1.update(dict2)
    print(dict1)  # {'a': 100, 'c': 3, 'b': 2, 'd': 4}

    # Обработка списков \ словарей
    list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
    list_b = [x for x in list_a if x % 2 == 0 and x > 0]
    # берем те x, которые одновременно четные и больше нуля
    print(list_b)  # [2, 4]

    #Например, можем посчитать квадраты значений каждого элемента:
    list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
    list_b = [x**2 for x in list_a]
    print(list_b)   # [4, 1, 0, 1, 4, 9, 16, 25]

    #Или посчитать длины строк c помощью функции len()
    list_a = ['a', 'abc', 'abcde']
    list_b = [len(x) for x in list_a]
    print(list_b)   # [1, 3, 5]

    list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
    list_b = [x if x < 0 else x ** 2 for x in list_a]
    # Если x-отрицательное - берем x, в остальных случаях - берем квадрат x
    print(list_b)  # [-2, -1, 0, 1, 4, 9, 16, 25]

    # Улучшаем читаемость
    numbers = range(10)
    # Before
    squared_evens = [n ** 2 for n in numbers if n % 2 == 0]
    # After
    squared_evens = [
        n ** 2
        for n in numbers
        if n % 2 == 0
    ]
    print(squared_evens)

    # Старый метод через лямбду
    numbers = range(10)
    squared_evens = map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers))
    print(squared_evens)  # <map object at 0x7f661e5dba20>
    print(list(squared_evens))  # [0, 4, 16, 36, 64]

    # Выражение-генератор - выдаёт по одному значению, пишется в круглых скобках, в то время как простой генератор
    # обозначается квадратными скобками, что логично, т.к. на выходе мы получаем список
    list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
    my_gen = (i for i in list_a)  # выражение-генератор
    print(next(my_gen))  # -2 - получаем очередной элемент генератора
    print(next(my_gen))  # -1 - получаем очередной элемент генератора

    # Переворачиваем словарь
    dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
    dict_123 = {v: k for k, v in dict_abc.items()}
    print(dict_123)  # {1: 'a', 2: 'b', 3: 'd'}
    # Обратите внимание, мы потеряли "с"! Так как значения были одинаковы,
    # то когда они стали ключами, только последнее значение сохранилось.

    # Словарь из списка
    list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
    dict_a = {x: x ** 2 for x in list_a}
    print(dict_a)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, -2: 4, -1: 1, 5: 25}