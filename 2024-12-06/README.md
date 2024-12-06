문자열 함수 <br>
replace() : 문자열 바꾸기, replace(바뀔문자열, 바꿀문자열)

참고 : https://wikidocs.net/11

---

리스트 컴프리헨션 <br>
간단하고 효율적인 방법으로 리스트를 생성

```
[expression for item in iterable if condition]
ex) squares = [x**2 for x in range(1, 11)]
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0] # if 사용하여 조건에 맞는 항목만 출력
```
