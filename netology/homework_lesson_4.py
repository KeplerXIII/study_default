from pprint import pprint


def task_1():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

    check_country = "Россия"

    # Моё решение, менее рациональное
    # geo_logs_temp = []
    # for dict in geo_logs:
    #     for values in dict.values():
    #         if check_country in values:
    #             geo_logs_temp.append(dict)
    # geo_logs = geo_logs_temp
    # pprint(geo_logs)
    # return geo_logs

    # Подсказка куратора, .values возвращает список, поэтому у меня не получалось, надо было взять
    # элемент из списка списков и проверять по нему.
    result_list = []
    for visit in geo_logs:
        if check_country in list(visit.values())[0]:
            result_list.append(visit)
    pprint(result_list)


def task_2():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    uniq_geo = list(set(sum(list(ids.values()), [])))
    print(uniq_geo)


def task_3():
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]

    result = {}
    avg_requests = len(queries)
    for request in queries:
        result.setdefault(len(request.split()), 0)
        result[len(request.split())] += 1
    for request_dict in result:
        pprint(f'Запросов состоящих из {request_dict} слов - {round(result[request_dict] / avg_requests * 100, 2)}%')


def task_4():
    # stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    # best_company = max(list(stats.values()))
    # stats_rev = {v: k for k, v in stats.items()}
    # pprint(stats_rev[best_company])
    #
    # Более рациональное решение от куратора сортируем по ключу.
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    best_company = max(stats, key=stats.get)
    pprint(best_company)


def task_5(list):
    if len(list) <= 1:
        return list[0]
    return {list[0]: task_5(list[1:])}
