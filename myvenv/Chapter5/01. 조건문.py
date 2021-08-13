#조건에 따라 명령을 실행시킴

def main():
  '''
  sub = int(input('현재 구독자 수를 입력하세요>>>'))
  if sub >= 1000:
    print('수익 창출이 가능합니다.')
  else:
    print('수익 창출이 불가능합니다.')
  '''
  challenge = int(input('공부시간:'))
  if challenge >= 10:
    print('잠금해제')
  elif 10 > challenge >= 5:
    print('30분 사용')
  else:
    print('사용x')
if __name__ == "__main__":
  main()