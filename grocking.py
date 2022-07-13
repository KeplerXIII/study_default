# Считаем сумму списка

def sum_(list_):
    if list_ == []:
        return 0
    return list_[0] + sum(list_[1:])


# Считаем количество элементов в списке


def count(list_):
    if list_ == []:
        return 0
    return 1 + count(list[1:])


# Наибольшее число в списке

def max_(list_):
    if len(list_) == 2:
        return list_[0] if list_[0] > list_[1] else list_[1]
    sub_max = max_(list_[1:])
    return list_[0] if list_[0] > sub_max else sub_max


# Быстрая сортировка

def quicksort(array):
    if len(array) < 2:
        return array  # Базовый случай
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]  # Подмассив элементов меньше опорного
        greater = [i for i in array[1:] if i > pivot]  # Подмассив элементов больше опорного
        return quicksort(less) + [pivot] + quicksort(greater)


# Получение сведения о наличии записи в словаре:

def check_dict():
    voted = {}
    value = voted.get("tom")
    print(value)


# Очередь

from collections import deque


def queue():
    search_queue = deque()
    search_queue += [2, 3, 4]
    print(search_queue.popleft())
    print(search_queue.popleft())


graph = {}
graph ["you"] = [ "alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(person):
    if person == "you":
        return True
    return False



def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person +" is а mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print("Not in search")
    return False

    search("you")
