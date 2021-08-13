#내장 모듈
#: 파이썬 설치시 자동으로 설치되는 모듈
from math import pi, ceil as c

print(pi)
print(c(2.7))

#외장 모듈
#: 다른 사람이 만든 모듈을 pip를 통해 사용
#pyautogui
import pyautogui as pg
pg.moveTo(500, 500, duration= 2)


