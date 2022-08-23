import requests
import time
from datetime import datetime

class Overflow:

    def two_days_question(self, page=1, i=0):
        url = "https://api.stackexchange.com/2.3/questions"
        date = str(round(time.time()) - 172800)
        self.page = page
        self.i = i
        params = {"fromdate": date,
                  "order": "desc",
                  "sort": "creation",
                  "tagged": "Python",
                  "site": "stackoverflow",
                  "pagesize": "100",
                  "page": page}

        response = requests.get(url, params=params)
        response = response.json()
        has_more = response['has_more']
        page += 1
        for item in response["items"]:
            i += 1
            print(datetime.fromtimestamp(item["creation_date"]).strftime("%A, %B %d, %Y %I:%M:%S"),
                  item["title"])
        if has_more:
            self.two_days_question(page + 1, i)
        else:
            print(f'Количество вопросов за 2 дня - {i}')
