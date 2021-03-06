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
print("I say \"Hello World\" ")
print("I say 'Hello world'")
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
str6 = str2[2:5]
print(str6)

str7 = str2[2:]
print(str7)

str8 = str2[:]
print(str8)

print('=============== 문자열 연산: 객체 함수 ==================')
# 대소문자 관련 함수
s = 'i like Python'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# 검색 관련 함수
s = 'I Like Python, I Like Deep Learning Also'
print(s.count("Like"))
print(s.find("Like"))
print(s.find("Like", 5))
print(s.find("AI"))
print(s.rfind("Like"))
try:
    print(s.index("AI"))
except ValueError as e:
    print('index() 함수는 발견하지 못하면 예외가 발생한다.')
print(s.rindex("Like"))
print(s.startswith("I Like"))
print(s.endswith("Also"))
print(s.endswith("Python", 0, 13))

# 편집 및 치환
s = '      spam and ham         '
print('----' + s. strip() + '----')
print('----' + s. rstrip() + '----')
print('----' + s. lstrip() + '----')

s = '<><><abc><><defg><><>'
print('----' + s. strip('<>') + '----')

s = 'Hello Java Java Java'
print(s.replace('Java','Python'))

# 분리
s = 'one:two:three:four'
r = s.split(':')
print(r, type(r))

r = s.split(':', 2)
print(r)

r = s.rsplit(':', 2)
print(r)

lines = """1st line
2nd line
3rd line
4th line
"""

r = lines.split('\n')
print(r)
# = print(lines.split('\n'))

r = lines.splitlines()
print(r)

# 결합
s = ' '.join(r)
print(s)

# 판별
print('1234'.isdigit())
print('abcd'.isalpha())
print('1234'.isalpha())
print('abcdefg'.islower())
print('ABCDEFG'.isupper())

print('=============== 문자열 연산: 포멧팅 ==================')
name = '둘리'
age = 10

# name: 둘리, age: 10
f1 = "name:" + name + ",age:" + str(10)
print(f1)

f2 = "name:" + format(name, 's') + ", age" + format(age, 'd')
print(f2)

f3 = "name: {}, age: {}"
print(f3.format(name, age))

f4 = "name: {1}, age: {0}"
print(f4.format(age, name))

f5 = f'name: {name}, age: {age}'
print(f5)





