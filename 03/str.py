# 한 줄 문자열
s1 = 'hello World'
s2 = "Hello World"
print(s1, type(s1), type(s2))

# 여러줄 문자 리터럴
#s2 = 'Hello\nWorld'
s3 = """Hello
World
"""
print(s3)

# 여러줄 주석을 대신하여 사용할 수 있다.
"""
주석1
주석2
주석3
"""

# escape(\ 붙어 있는 문자) 문자열
print('=============== escape ==================')
print('Hello\nWorld')
print("I say \'Hello World\' ")
print("I sat 'Hello world'")
print("둘리\t010-0000-0000")

print('=============== 문자열 연산: 길이 ==================')
print(len(s1))

print('=============== 문자열 연산: 반복 ==================')
str1 = 'First String'
str2 = 'Second String'

str3 = str1 * 3
print(str3)

print('=============== 문자열 연산: 인덱싱 ==================')
print(str1[0], str1[2], str1[3], str1[11])
# IndexError: string index out of range
# print(str1[12])

print('=============== 문자열 연산: 연결 concat ==================')
str4 = str1 + '\t' + str2
print(str4)

# 리터럴들을 연결할 때에는 + 생략 가능
str5 = 'hello' ' ' 'World'
print(str5)

# 문자열 객체와 정수 객체는 + 연산을 할 수 없다.
name = '둘리'
age = 10
#print(name + age)

print(name + ' ' +str(age))

print('=============== 문자열 연산: in, not in ==================')
print("S" in str1)
print("S" not in str2)

print('=============== 문자열 객체는 변경할 수 없다.(immutable) ==================')
# str1[0] = 'f'
# print(str0)

print('=============== 문자열 연산: 슬라이싱 ==================')


print('=============== 문자열 연산: 객체 함수 ==================')


print('=============== 문자열 연산: 포멧팅 ==================')
"""epoch = 1000
init = (0,0)
diff = 10

"epoch=" + str(100) + "회 초기값" + str(init)

f'epoch=회, 초기값: {init}'
"""


