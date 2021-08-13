#raise 구문을 사용하여 강제로 에러 발생 시키기

try:
  num = int(input('음수:'))
  if num >= 0:
    raise ValueError('양수 입력 불가')
except ValueError as e:
  print("예외 발생", e)