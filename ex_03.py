# 버퍼에 대한 이해
# 백준문제


# -------------------> 최대 15글자
# 총 5줄
# | A A B C D D
# | a f z z 
# | 0 9 1 2 1
# | a 8 E W g 6
# | P 5 h 3 k x

# input                         

# ABCDE
# abcde
# 01234
# FGHIJ
# fghij

# output
# Aa0FfBb1GgCc2HhDd3IiEe4Jj


s = [[] for i in range(15)]

for i in range(5):
    t = input().strip()
    for j in range(len(t)):
        s[j].append(t[j])

for i in range(15):
    if i == []:
        break
    print(''.join(s[i]), end='')