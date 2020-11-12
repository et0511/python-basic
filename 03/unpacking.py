# packing은 tuple로만 가능하다.
print('========== packing ===========')
t = 10, 20, 30, 'python'
print(t, type(t))

print('========== unpacking ===========')
a, b, c, d = t
print(a, b, c, d)

# 오류: 패킹되어 있는 객체가 더 많은 경우
# a, b, c = t
# 오류: 패킹되어 있는 객체가 더 적은 경우
# a, b, c, d, e = t

print('========== 확장 ===========')
t = (1, 2, 3, 4, 5)
a, *b = t  # *는 나머지를 하나로 묶는 역할
print(a, b)

*a, b = t
print(a, b)

a, *b, c = t
print(a, b, c)




