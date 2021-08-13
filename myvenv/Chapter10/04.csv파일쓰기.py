import csv
data = [
  ["이름",'반','번호'],
  ["재석", 1, 20],
  ["홍철", 3, 8],
  ["형돈", 5 ,32]
]
#newline은 윈도우에서 csv파일 생성이 자동으로 한 줄씩 띄워주는 걸 막는다.
file = open('./myvenv/Chapter10/student.csv', 'w', newline= '', encoding = 'utf-8-sig')
writer = csv.writer(file)

for d in data:
  writer.writerow(d)
file.close()

