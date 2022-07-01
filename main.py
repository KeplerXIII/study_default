from decorator_timecheck import decor
from decorator_timecheck import time_check


@time_check
@decor
def printer():
    result = sum(range(0, 100000000))
    print(result)


printer()
