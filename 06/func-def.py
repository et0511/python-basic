# 함수 정의
print('========== 함수 정의 ===========')

def dummy():
    pass        # 아무것도 안하는 블록을 만듬


def func1(a):
    print('Hello World')


def func2(name):
    print('Hello' + name)


def func3(b):
    b = 'HW'
#    return'Hello World'

a = 'ggg'
print(a)
func3('a')
b = func3('a')
print(a)

def times(a, b):
    return a * b


#dummy()
#func1()
#func2('강신원')
#s = func3()
#n = times(2, 2)
#print(s, n)


print('========== 여러 값을 반환할 수 있다. ===========')

def func4():
    return 10, 20   # tuple auto packing을 통해 튜플 객체 하나를 반환한다.

a, b = func4()      # tuple auto packing을 통해 반환된 튜플 객체를 여러 변수에 대입할 수 있다.
print(a, b)


print('========== 함수도 객체다. ===========')

print(func1)
print(type(func1))
f = func1
f()

