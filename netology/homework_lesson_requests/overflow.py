import requests
import time
from datetime import datetime

class Overflow:

    def two_days_question(self):
        url = "https://api.stackexchange.com/2.3/questions"
        date = str(round(time.time()) - 172800)
        params = {"fromdate": date,
                  "order": "desc",
                  "sort": "creation",
                  "tagged": "Python",
                  "site": "stackoverflow",
                  "pagesize": "100"}
        response = requests.get(url, params=params)
        response = response.json()
        i = 0
        for item in response["items"]:
            i += 1
            print(datetime.fromtimestamp(item["creation_date"]).strftime("%A, %B %d, %Y %I:%M:%S"), item["title"])
        print(f'Количество строк {i}')