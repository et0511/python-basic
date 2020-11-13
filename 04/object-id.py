# object ID

i1 = 10
i2 = 20
print(hex(id(i1)), hex(id(i2)))

i1 = 12334567890
i2 = 12334567890
print(hex(id(i1)), hex(id(i2)))


l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)), hex(id(l2)))

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

print(i1 is i2)
print(l1 is l2)
print(l1 == l2)
print(s1 is s2)

# ?월요일에 추가 설명?
import sys

t1 = (1, 2, 3, 4, 5)
t2 = (1, 2, 3, 4, 5)
print(sys.getrefcount(t1))
print(t1 is t2)

t3 = t1
print(sys.getrefcount(t1))
