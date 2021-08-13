class airconditioner():
  def __init__(self, volt, O_u, display):
    self.volt = volt
    self.O_u = O_u
    self.display = display
  
  def set_volt(self, volt):
    if volt >= 220:
      print('turn on the air conditioner')
      return 1
    else:
      print('전력부족')
      return 0

  def set_O_u(self, volt):
    if volt == 1:
      print('turn on the O_u')
      return 1
    else:
      print('전력부족')
      return 0
  
  def set_display(self, volt, O_u):
    if volt == 1 and O_u == 1:
      print('온도와 바람세기를 설정해주세요.')
    else:
      print('전력이 부족합니다.')

class display():
  def __init__(self, set_temp, wind_power, Current_temp):
    self.set_temp = set_temp
    self.wind_power = wind_power
    self.Current_temp = Current_temp
  
  def set_wind(self, wind_power):
    print(f"{wind_power}로 바람을 설정합니다.")
    return wind_power

  def set_temp(self, set_temp):
    print(f"{set_temp}로 온도를 설정합니다.")
  
  def get_Current_temp(self, Current_temp):
    pass