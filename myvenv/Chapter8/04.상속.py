'''상속
  -> 클래스 간의 중복을 해소하고 유지보수를 편하게 하기 위해 사용
  -> 부모 클래스에 중복되는 부분, 자식 클래스에는 각각 다른 특징 적용
'''

#부모 클래스
class Monster():
  def __init__(self, name, attack, health):
    self.name = name
    self.attack = attack
    self.health = health
  def move(self):
    print(f"[{self.name}] 지상에서 이동하기")
#자식 클래스
class Wolf(Monster):
  pass

class Shark(Monster): #메서드 오버라이딩-> 메소드 재정의/ 부모인 monster의 메소드를 재정의하여 사용
  def move(self):
    print(f"[{self.name}] 헤엄치기")
    
class Dragon(Monster):
  def move(self):
    print(f"[{self.name}] 날기")

wolf = Wolf('Wolf', 70, 100)
wolf.move()
shark = Shark('Shark', 80, 230)
shark.move()
dragon = Dragon('Dragon', 90, 300)
dragon.move()

