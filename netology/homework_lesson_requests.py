import requests

def most_intellegence(compare_list):
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    data = requests.get(url)
    heroes = data.json()
    compare_dict = {}
    for hero in heroes:
        if hero["name"] in compare_list:
            compare_dict[hero["name"]] = hero["powerstats"]["intelligence"]

    print(f'Самый умный тут у нас - мистер {max(compare_dict, key=compare_dict.get)}')

most_intellegence(["Hulk", "Captain America", "Thanos"])