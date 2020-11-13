# 문자열 데이터를 분석(학습)하기 전 처리할 수 만들기
# 1. 공백제거
# 2. 필요 없는 문장 부호 빼기
# 3. 대소문자 정리(Capitalize 처리)


import re

states = ['alabama', 'Georgia!', 'Georgia','Georgia','Georgia', ' FlorIda', 'south carolina', 'West virginia?']

def clean_strings(strings):
    results = []
    for string in strings:
        string = string.strip()                 # 1
        string = re.sub('[!#?]', '', string)    # 2
        string = string.title()                 # 3

        results.append(string)

    return results

states = clean_strings(states)
print(states)


###############################################################################
# data1 -> f1() -> data2 -> f2() -> data2 -> f3() -> data3(final)
states = ['alabama', 'Georgia!', 'Georgia', 'Georgia', 'Georgia', ' FlorIda', 'south carolina', 'West virginia?']

def title(string):
    return string.title()


def remove_specialch(s):
    return re.sub('[!#?]', '', s)


def strip(s):
    return s.strip()


def clean_string(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)

        results.append(string)
    return results

states = clean_string(states, strip, remove_specialch, title)
print(states)




