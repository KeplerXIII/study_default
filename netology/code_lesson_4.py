# Множества кортежи словари

some_oxy_text = '''
Весь мой рэп, если коротко, про то, что
Уж который год который город под подошвой
В гору, когда прет. Потом под гору, когда тошно
Я не то, что Гулливер, но все же город под подошвой
Город под подошвой, город под подошвой
Светофоры, госпошлины, сборы и таможни
Я не знаю, вброд или на дно эта дорожка
Ты живешь под каблуком, у меня - город под подошвой
'''

res = {}

for word in some_oxy_text.lower().replace('-', '').split():
  word = word.strip(',!.?')
  # print(word)
  res.setdefault(word, 0)
  res[word] += 1