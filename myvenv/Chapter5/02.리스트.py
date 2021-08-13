''' 
1. 리스트 만들기
ex) ani = [~,~,~]

2. 공백 리스트
a = []

3. 데이터 접근
ani[~]
0부터 시작

4. 데이터 추가
li.append()

5. 데이터 할당
li[1] = '~'

6. 데이터 삭제
del list[삭제할 자료의 인덱스 번호]
list.remove(지울 아이템)
7. 슬라이싱
list[first:last] 

8. 길이
len(list) 길이 반환

9. 리스트 정렬
list.sort() 오름차순 
list.sort(reverse = True) 내림차순
'''

def main():
  '''1.
  result = [33, 40, 12, 63, 52]
  result.append(9)
  print(result)

  result[1] = 50
  print(result)

  print(result[2:6])
  result.sort()
  print(result)
  '''
  res = []
  sum = 0
  for i in range(7):
    x = int(input('{}일차 턱걸이 횟수>>>'.format(i+1)))
    res.append(x) 
    sum += x
  print(int(sum/7))
if __name__ == "__main__":
  main()