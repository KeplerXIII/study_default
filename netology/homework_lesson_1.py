def task_1():
    l = int(input("Введите длину стороны квадрата: "))
    square_perimetr = l * 4
    square_area = l ** 2
    print(f'Периметр: {square_perimetr}')
    print(f'Площадь: {square_area}')

    l = int(input("Введите ширину прямоугольника: "))
    h = int(input("Введите высоту прямоугольника: "))
    rectangle_perimetr = (l + h) * 2
    rectangle_area = l * h
    print(f'Периметр: {rectangle_perimetr}')
    print(f'Площадь: {rectangle_area}')

    # Задача №3 - разделитель
    len_divider = square_perimetr + rectangle_area
    divider = input("Введите символ разделителя: ")
    print(divider * len_divider)


def task_2():
    salary = int(input("Введите заработную плату в месяц: "))
    credit = int(input("Введите, какой процент(%) уходит на ипотеку: "))
    daily = int(input("Введите, какой процент(%) уходит на жизнь: "))

    print(f'На ипотеку было потрачено: {int(salary * credit / 100) * 12} рублей за год')
    print(f'Было накоплено: {int(salary - (salary * credit / 100 + salary * daily / 100)) * 12} рублей за год')


task_1()
task_2()