from YYJ import GPIO_RPi
from YYJ import Vision
import time

#初始化L298N驱动
L= GPIO_RPi.L298N(18,16,35,37,33,31)
L.Stop()
L.Forward(50,50)
# L.TurnLeft(50,50)
time.sleep(2)
L.Stop()
print('stop')