#아이템 기획
#부모 클래스
class Item():
  def __init__(self, name, price, weight, isdropable):
    self.name = name
    self.price = price
    self.weight = weight
    self.isdropable = isdropable
  def sale(self):
    print(f'[{self.name}]을 {self.price}에 판매합니다.')
    
  def discard(self):
    if self.isdropalbe:
      print(f'[{self.name}]을 버립니다.')
    else:
      print(f'[{self.name}]을 버릴 수 없습니다.')

#자식 클래스
class WearableItem(Item):
  def __init__(self, name, price, weight, isdropable, Wear_effect):
    super().__init__(name, price, weight, isdropable)
    self.effect = Wear_effect
  def wear(self):
    print(f'[{self.name}]을 착용합니다.')

#자식 클래스
class UseableItem(Item):
  def __init__(self, name, price, weight, isdropable, Use_effect):
    super().__init__(name, price, weight, isdropable)
    self.effect = Use_effect
  def use(self):
    print(f'[{self.name}]을 사용합니다.')  
  