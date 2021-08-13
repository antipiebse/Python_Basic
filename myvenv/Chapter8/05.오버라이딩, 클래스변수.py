import random
#부모 클래스

#클래스 변수
# : 인스턴스들이 모두 공유하는 변수
class Monster():
  Max_num = 1000 #클래스 변수 생성
  def __init__(self, name, attack, health):
    self.name = name
    self.attack = attack
    self.health = health
    Monster.Max_num -= 1 #클래스 변수
  def move(self):
    print(f"[{self.name}] 지상에서 이동하기")
#자식 클래스
class Wolf(Monster):
  pass

class Shark(Monster): #메서드 오버라이딩-> 메소드 재정의/ 부모인 monster의 메소드를 재정의하여 사용
  def move(self):
    print(f"[{self.name}] 헤엄치기")
    
class Dragon(Monster):
    #생성자 오버라이딩
  def __init__(self, name, attack, health):
    super().__init__(name, attack, health) #super를 사용하면 그대로 부모의 속성을 가져올 수 있음.
    self.skills = ('불뿜기','꼬리치기', '날개치기')
  def move(self):
    print(f"[{self.name}] 날기")
  def skill(self):
    print(f'[{self.name}]이 스킬을 사용하였습니다. {self.skills[random.randrange(0,2)]} ')

wolf = Wolf('Wolf', 70, 100)
wolf.move()
shark = Shark('Shark', 80, 230)
shark.move()
dragon = Dragon('Dragon', 90, 300)
dragon.move()
dragon.skill()

