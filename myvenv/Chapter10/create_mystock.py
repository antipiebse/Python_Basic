#my stock을 만드는 파일
def main():
  import csv
  data = [
  ['종목', '매입가', '수량', '목표가'],
  ['삼성전자', 85000, 10 ,90000],
  ['NAVER', 380000, 5 , 400000]
  ]
  #csv 파일 생성후 저장
  with open('./myvenv/Chapter10/mystock.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    for i in data:
      writer.writerow(i)

if __name__ =="__main__":
  main()