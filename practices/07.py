# 문제 7.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
s = 0
count = 5
l = list()
sum = 0
# for c in range(count):
#     n = int(input(f'[{c+1}]>'))
#    l.append(n)
# print()

number = 0
sum = 0
for c in range(count):
    n = int(input(f'[{c + 1}]>'))
    s = s + 1
    sum = sum + n
print(sum / s)







