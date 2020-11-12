print('========== zip() 함수 사용 예 ===========')

s1 = ['foo', 'bar', 'baz']
s2 = ['one', 'two', 'three', 'four']

z = zip(s1, s2)
print(z, type(z))

print('========== 순회1 ===========')
for t in z:
    print(t, type(t))

z = zip(s1, s2)
for a, b in z:
    print(a, b)

print('========== 순회2 ===========')
z = zip(s1, s2)






