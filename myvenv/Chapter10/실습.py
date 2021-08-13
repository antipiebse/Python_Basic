import csv
import create_mystock

create_mystock.main()
#csv 파일 읽어와서 표현
with open('./myvenv/Chapter10/mystock.csv', 'r', encoding='utf-8', newline='') as file:
  goal = []
  Purchase_price = []
  Quantity = []
  proceeds = []
  my_yield = []
  company = []
  #매입가, 수량, 목표가 리스트 생성
  reader = csv.reader(file)
  for data in reader:
    company.append(data[0])
    if data[1].isdigit():
      Purchase_price.append(int(data[1]))
    if data[2].isdigit():
      Quantity.append(int(data[2]))
    if data[3].isdigit():
      goal.append(int(data[3]))
  i = 0
  while i != 2:
    proceeds.append((goal[i] - Purchase_price[i]) * Quantity[i])
    my_yield.append((goal[i]/Purchase_price[i]-1) * 100)
    print(f'{company[i+1]}, {proceeds[i]}, {my_yield[i]:.3}')
    i += 1


    

