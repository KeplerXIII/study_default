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
    my_files_sorted = sorted(my_files, key=len) # сортировка по длине
    print(my_files_sorted)  # ['pc.png', 'apple.bmp', 'mydog.gif', 'somecat.jpg']

    my_set = {2, 5, 1, 7, 3}
    my_set_sorted = sorted(my_set, reverse=True)
    print(my_set_sorted)  # [7, 5, 3, 2, 1]
