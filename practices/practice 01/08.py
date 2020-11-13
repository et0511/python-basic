# 문제8.
# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

#str = input('문자를 입력하세요.: ')
#a = [1, 2, 3, 4]
#a.reverse()
#print(a)

l = input('문자를 입력하세요.: ')
b = ''
for r in l:
    b = r + b

print(b)

# l = input('문자를 입력하세요.: ')
# print(l[::-1])
