# if ~ else : 기거나 아니거
print('========= if ~ elif : 기거나 아니거나 ===========')
a = 10

if a > 5:
    print('big')
else:
    print('small')

print('========= if ~ elif ~ else ===========')
b = 10
if b > 0:
    print('양수')
elif b < 0:
    print('음수')
else:
    print('0')

order = 'spagetti'
price = 0
# spam price: 1000
# milk price: 500
# eff price: 100
if order =='spam':
    price = 1000
elif order == 'milk':
    price = 500
elif order == 'eff':
    price = 100
else:
    price = '없는 상품'

print(f'가격: {price}')



print('========= if ~ elif ~ else ===========')


