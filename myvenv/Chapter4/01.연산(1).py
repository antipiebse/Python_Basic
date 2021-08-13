# 1.  대입연산
# 변수이름 = 데이터

# 2. 산술연산
# - 숫자 연산
x = 5
y = 2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)

# - 문자열 연산
tag1 = "#파이썬"
tag2 = "#백엔드 공부"
tag3 = "#fastapi"

tag = tag1 + tag2 + tag3
print(tag)

message = "파이썬 공부 파이팅\n" *5
print(message)

# 복합 할당 연산자
level = 10 #레벨 1 증가
level += 1 #level = level + 1

health = 2000
health -= 300

attack = 300
attack *= 1.5

speed = 420
speed /= 2 
print(level, health, attack, speed)