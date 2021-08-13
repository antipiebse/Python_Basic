# 1. import 패키지.모듈
import unit.character
unit.character.test()

# 2. from 패키지 import 모듈
from unit import item
item.test()

# 3. from 패키지 import * 패키지 안의 모듈을 다 불러옴, 그러나 init파일을 편집해야함.
from unit import *
character.test()
item.test()
monster.test()

# 4. import 패키지
import unit
unit.character.test()
unit.monster.test()
unit.item.test()