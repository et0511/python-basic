# 문제9.
# 주어진 if 문을 dict를 사용해서 수정하세요.

menu = input('메뉴: ')
m = {'오뎅': '300', '순대': '400', '만두': '500'}
o = {key: value for key, value in dict.fromkeys(keys).items()}

p = m.get('menu')
print(p(f'가격: {0}'))
