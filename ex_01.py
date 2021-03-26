# 컴퓨터 공학개론 예제파일 #
# 20210306


# 3 x 5 ㄱ 출력
for i in range(3):
    for j in range(5):
        if i == 0 or j == 4:
            print('o', end='')
        else:
            print(' ', end='')
    print()

# 3 x 5 ㅅ 출력
for i in range(3):
    f, b = ' ' * (2-i), ' ' * (2*i-1)
    if i==0:
        print(f + 'o')
    else:
        print(f + 'o' + b + 'o')

# n 입력
n = int(input())

# n ㄱ 출력

for i in range(n):
    for j in range(n*2-1):
        if i == 0 or j == n*2-2: # ->방향으로는 보기좋게 적절히 설정
            print('o', end='')
        else:
            print(' ', end='')
    print()

# n ㅅ 출력 파이썬 특징 이용
for i in range(n):
    f, b = ' ' * (n-1-i), ' ' * (2*i-1)
    if i==0:
        print(f + 'o')
    else:
        print(f + 'o' + b + 'o')

# n ㅅ 출력 i와 j의 관계를 이용한 방법
for i in range(n):
    for j in range(n*2-1):
        if i+j == n-1 or i == j - (n-1):
            print('o', end='')
        else:
            print(' ', end='')
    print()

# 함수이용

def giyoek(n):
    for i in range(n):
        for j in range(n * 2 - 1):
            if i == 0 or j == n * 2 - 2:  # ->방향으로는 보기좋게 적절히 설정
                print('o', end='')
            else:
                print(' ', end='')
        print()

def siot(n):
    for i in range(n):
        f, b = ' ' * (n - 1 - i), ' ' * (2 * i - 1)
        if i == 0:
            print(f + 'o')
        else:
            print(f + 'o' + b + 'o')


# ㅅㄱㅅㄱ

giyoek(n)
siot(n)
giyoek(n)
siot(n)

# 자음 모음 추가 받습니다