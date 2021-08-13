#결제 정보, 관리 모듈
#변수
version = 2.0

#함수
def printAuthor():
  print('문성민')

class Pay():
  def __init__(self, id, price, time):
    self.id = id
    self.price = price
    self.time = time
  def get_pay_info(self):
    return f"{self.id} {self.price} {self.time}"
    
if __name__ == "__main__":
  print('pay module 실행')
print(__name__)