'''정리
 1. 사용자로부터 입력받기
  -> input()
  
 2. 자료형 변환
 int, str, float....'''
#자료형 확인: type(x) 
def main():
  num1 = int(input('첫 번째 숫자를 입력하세요:'))
  num2 = int(input('두 번째 숫자를 입력하세요:'))
  sum = num1 + num2 
  print(sum)
  age()
def age():
  past = int(input('태어난 년도:'))
  now = 2021
  res = now - past + 1
  print('현재 나이는 {}'.format(res))
if __name__ == "__main__":
  main()