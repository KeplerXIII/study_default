def is_palindrome(n):
    x, y = n, 0
    f = lambda: (y * 10) + x % 10
    while x > 0:
        x, y = x//10 , f()
    return y == n

number = int(input())


def isPalindrome(x):
        if x < 0 or (x > 0 and x%10 == 0):
            return False
        reversedNum = 0
        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10
            x = x // 10
            print(x, reversedNum) #проверка
        return True if (x == reversedNum or x == reversedNum // 10) else False

def is_palindrome(n):
    x, y = n, 0
    f = lambda: (y * 10) + x % 10
    while x > 0:
        x, y = x//10 , f()
        print(x, y)
    return y == n

number = int(input())
print(is_palindrome(number))