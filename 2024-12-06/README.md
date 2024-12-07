### 문자열 함수 <br>
replace() : 문자열 바꾸기, replace(바뀔문자열, 바꿀문자열)

참고 : https://wikidocs.net/11

---

### 리스트 컴프리헨션 <br>
간단하고 효율적인 방법으로 리스트를 생성

```
[expression for item in iterable if condition]
ex) squares = [x**2 for x in range(1, 11)]
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0] # if 사용하여 조건에 맞는 항목만 출력
```
 ---
 ### 배열 정렬
- sort(): 리스트 메서드, 원본 수정, None 반환, 리스트를 직접 정렬하고 싶다
- sorted(): 내장 함수, 새 리스트 반환, 원본 유지, 원본은 그대로 두고 새 정렬된 리스트가 필요하다

```
numbers = [3, 1, 4, 1, 5, 9, 2]
result = numbers.sort()  # result는 None
print(result)  # None
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

numbers = [3, 1, 4, 1, 5, 9, 2]
result = sorted(numbers)  # result는 새로운 정렬된 리스트
print(result)  # [1, 1, 2, 3, 4, 5, 9]
print(numbers)  # [3, 1, 4, 1, 5, 9, 2] (원본 유지)
# 추가 옵션: 역순 정렬
print(sorted(numbers, reverse=True))  # [9, 5, 4, 3, 2, 1, 1]
```
