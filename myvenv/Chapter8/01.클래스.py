#클래스와 객체
'''클래스-> 설계도, 객체 -> 설계도를 통해 만들어낸 제품
  클래스는 속성(특징)과 메소드(동작)의 집합'''

class Monster():
  def say(self):
    print('나는 몬스터다!')
goblin = Monster()
goblin.say()

#파이썬에서는 자료형도 클래스이다.
a = 10
b = 'hello'
c = True
print(type(a))
print(type(b))
print(type(c))

print(b.__dir__())