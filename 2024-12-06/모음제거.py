def solution(my_string):
    answer = ''
    # 문자열 하나하나 반복
    for i in my_string:
        # 모음 배열 안 글자가 있으면 공백으로 대체
        if i in ['a', 'e', 'i', 'o', 'u']:
          my_string = my_string.replace(i, '')
    
    answer = my_string
    return answer

# return "".join([i for i in my_string if not(i in "aeiou")])