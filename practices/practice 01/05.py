# 문제5.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.(for~in)
lst = [10, 12, 14, 15, 17, 18, 19, 20, 25, 30, 32, 33, 37, 40, 42, 44, 46, 50]
count = 0
s = 0
for n in lst:
    if n % 3 == 0:
        count = count + 1
        s = s + n
    else:
        continue


print(f'3의 배수의 갯수:{count}, 3의 배수의 합:{s}')



kount = 0
s1 = 0
for t in range(1000):
    if t % 2 == 0:
        kount = kount + 1
        s1 = s1 + t

print(f'2의 배수의 개수: {kount}, 2의 배수의 합: {s1}')