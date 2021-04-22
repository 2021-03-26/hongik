# 팩토리얼의 구현
import time
start = time.time()

def factorial(n:int) -> int:
    if n==0 or n==1:
        return 1
    else:
        s = 1
        for i in range(1, n+1):
            s *= i
        return s

for i in range(1000000):
    factorial(100)


print("걸린시간 ", time.time()-start)


start = time.time()

def _factorial(n:int) -> int:
    if n==0 or n==1:
        return 1
    else:
        return n*_factorial(n-1)

for i in range(1000000):
    factorial(100)


print("걸린시간 ", time.time()-start)

fact = {}

def __factorial(n):
    if n<2:
        return 1
    if n not in fact:
        fact[n] = n * __factorial(n-1)
    return fact[n]

def decorater(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print("걸린시간 ", time.time()-start)
    return wrapper


@decorater
def __check():
    for i in range(1000000):
        __factorial(100)

# 데코레이터


__check()


