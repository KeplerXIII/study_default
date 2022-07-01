def task1():
    discounts = {
        "vostok": 2,
        "children": 3,
        "project": 0.5,
        "insurance": 1.5
    }

    basic = int(input("Введите базовую ставку: "))
    childrens = int(input("Введите количество детей: "))
    region = input("Коэффициент Дальнего Востока(да\нет): ")
    salary_project = input("Является ли участником зарплатного проекта(да\нет): ")
    insurance_project = input("Застрахован(да\нет): ")

    avarage_percent = basic

    if region == "да":
        avarage_percent -= discounts["vostok"]
    if childrens > 3:
        avarage_percent -= discounts["children"]
    if salary_project == "да":
        avarage_percent -= discounts["project"]
    if insurance_project == "да":
        avarage_percent -= discounts["insurance"]

    print(avarage_percent)


def task2():
    # day_in_months = {
    #  "январь": 31,
    #  "февраль": 28,
    #  "март": 31,
    #  "апрель": 30,
    #  "май": 31,
    #  "июнь": 30,
    #  "июль": 31,
    #  "август": 31,
    #  "сентябрь": 30,
    #  "октябрь": 31,
    #  "ноябрь": 30,
    #  "декабрь": 31
    # }

    # month = input("Введите месяц: ")
    # date = int(input("Введите день: "))
    # days = 0

    # for month_in_dict in day_in_months:
    #  days += day_in_months[month_in_dict]
    #  if month_in_dict == month:
    #    days += date - day_in_months[month]
    #    break

    # в разных источниках разные даты (поэтому дни могут различаться, считал своим же калькулятором дней при написании), логика - считаем дни и используем операторы с днями, для того, что бы условия в операторах были короче

    # if 50 >= days >= 20:
    #   print("Ваш знак зодиака: Водолей")
    # elif 79 >= days >= 51:
    #   print("Ваш знак зодиака: Рыбы")
    # elif 109 >= days >= 80:
    #   print("Ваш знак зодиака: Овен")
    # elif 140 >= days >= 110:
    #   print("Ваш знак зодиака: Телец")
    # elif 171 >= days >= 141:
    #   print("Ваш знак зодиака: Близнецы")
    # elif 203 >= days >= 172:
    #   print("Ваш знак зодиака: Рак")
    # elif 234 >= days >= 204:
    #   print("Ваш знак зодиака: Лев")
    # elif 265 >= days >= 235:
    #   print("Ваш знак зодиака: Дева")
    # elif 296 >= days >= 266:
    #   print("Ваш знак зодиака: Весы")
    # elif 326 >= days >= 297:
    #   print("Ваш знак зодиака: Скорпион")
    # elif 355 >= days >= 327:
    #   print("Ваш знак зодиака: Стрелец")
    # else:
    #   print("Ваш знак зодиака: Козерог")

    signs = {
        "март": (21, "Рыбы", "Овен"),
        "апрель": (21, "Овен", "Телец"),
        "май": (22, "Телец", "Близнецы"),
        "июнь": (22, "Близнецы", "Рак"),
        "июль": (23, "Рак", "Лев"),
        "август": (24, "Лев", "Дева"),
        "сентябрь": (24, "Дева", "Весы"),
        "октябрь": (24, "Весы", "Скорпион"),
        "ноябрь": (23, "Скорпион", "Стрелец"),
        "декабрь": (23, "Стрелец", "Козерог"),
        "январь": (21, "Козерог", "Водолей"),
        "февраль": (20, "Водолей", "Рыбы")
    }

    day = int(input("Input day: "))
    month = input("Input month: ")

    if (day >= signs[month][0]):
        print(signs[month][2])
    else:
        print(signs[month][1])


# task1()
task2()
