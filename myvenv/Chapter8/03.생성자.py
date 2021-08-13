''' 생성자
    : 인스턴스를 만들 때 호출되는 메소드'''

class Monster:
  def __init__(self, health, attack, speed):
    self.health = health
    self.attack = attack
    self.speed = speed  
  def decrease_health(self, health):
    self.health -= health
  def get_health(self):
    return self.health

#고블린 인스턴스
goblin = Monster(700, 65, 100)
print(goblin.health)
goblin.decrease_health(100)
print(goblin.get_health())

#늑대 인스턴스
wolf = Monster(800, 90, 120)
wolf.decrease_health(29)
print(wolf.get_health())
