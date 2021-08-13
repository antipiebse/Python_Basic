'''파일 입출력을 사용하는 이유
  - 파일로부터 데이터를 읽어와서 프로그램에 사용하기 위해
  - 프로그램에서 만든 데이터를 파일형태로 저장하기 위해
 w: 쓰기, r: 읽기, a: 추가
'''
# 1. 파일 쓰기
file = open('./myvenv/Chapter10/data.txt','w', encoding='utf8')
file.write('hello')
file.close()

# 2. 파일 추가
file = open('./myvenv/Chapter10/data.txt','a', encoding='utf8')
file.write('\n코딩하자')
file.close()

# 3. 파일 읽기
file = open('./myvenv/Chapter10/data.txt','r', encoding='utf8')

# 3.1 파일 전체 읽기
#data = file.read()
#print(data)
#file.close()

# 3.2 파일 한 줄 읽기
while True:
  data = file.readline()
  print(data, end = "")
  if data == '':
    break
file.close()
