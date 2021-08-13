#환전

won = input('원화 금액을 입력하세요: ')
dollar = input('환율을 입력하세요: ')

try: #예외가 발생할 수 있는 코드
  print(int(won)/ int(dollar))
except ValueError as e: #예외 발생 시 실행되는 코드
  print('문자열 오류.' , e)
except ZeroDivisionError as e:
  print('나누기 0 불가능', e)

else: #에러가 발생하지 않았을 때 실행
  print('no error')

finally: #항상 실행되는 코드, 주로 리소스 반환이나 파일 닫기 시 사용
  print('끝!')