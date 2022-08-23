from ya_disk import YandexDisk
from overflow import Overflow
from user import _token
from most_intelligence import most_intellegence

TOKEN = _token

if __name__ == '__main__':
    ya = YandexDisk(token=_token)
    ya.upload_file_to_disk("test/test.txt", "test.txt")

    print("\n\n")

    over = Overflow()
    over.two_days_question()

    print("\n\n")

    heroes = ["Thanos", "Captain America", "Hulk"]
    most_intellegence(heroes)
