# 문제2
# 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.

try:
    number = int(input('수를 입력하세요:'))
except ValueError as e:
    print('정수가 아닙니다.')
else:
    if number % 2 == 0:
        print('짝수입니다')
    else:
        print('홀수입니다.')