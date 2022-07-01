import time

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap


# def print_text():
# print("Hello world!")

# decorated = decor(print_text)
# decorated()

def time_check(func):
    def wrap():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(f'Выполнение функции заняло: {end - start:0.10f} секунд')

    return wrap


def reverse(text):
    i = 0
    result = ""
    while i < len(text):
        result = text[i] + result
        i += 1
    return result


@time_check
def reverse_text():
    text = "Hello petya"
    reverse(text)
    print(reverse(text))
