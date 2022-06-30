from datetime import datetime

#start = datetime.now()
#do_time = start - datetime.now()

#def decor(func):
#  def wrap ():
#    print("============")
#    func()
#    print("============")
#  return wrap


#def print_text():
# print("Hello world!")

#decorated = decor(print_text)
#decorated()

def time_check(func):
  def wrap ():
    start = datetime.now()
    func()
    print(datetime.now() - start)
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


reverse_text()