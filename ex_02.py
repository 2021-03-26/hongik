# dict 활용
# dict 과 map, zip을 이용해봅시당


# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#
#

# input
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 221 222 223 224 225 226
# XYZ

# output
# 456
# 일의 자리수만 뽑아서 매칭

my_dict = dict()
before = [chr(ord('A')+i) for i in range(26)]
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z


after = list(map(lambda x: int(x)%10 , input().split()))
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
# after = [after[i]%10 for i in range(len(after))]

for k, v in zip(before, after):
    my_dict.setdefault(k, v)

test = input()


for i in test:
    print(my_dict[i], end='') 