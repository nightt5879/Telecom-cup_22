from YYJ import GPIO_RPi
from YYJ import Vision
#陀螺仪需要的库
import smbus
import math

import time

# 电源控制寄存器地址
power_regist = 0x6b

# I2C模块初始化
bus = smbus.SMBus(1)
# 外接I2C设备的地址
address = 0x68

#初始化L298N驱动
L= GPIO_RPi.L298N(18,16,35,37,33,31)
L.Stop()
#初始化摄像头
Cam =  Vision.Camera(0, 320, 240)

#初始化三个红外
InL = GPIO_RPi.IO(38, 'IN')
InR = GPIO_RPi.IO(40, 'IN')
InM = GPIO_RPi.IO(36, 'IN')

def PIDControl(K,Kp, Ki, Kd, DeltaNow, ErrorSum ,DeltaLast):  #当下的误差
    P = Kp * DeltaNow
    
    I = Ki * ErrorSum
    
    ErrorOne = DeltaNow - DeltaLast  #误差偏移的梯度
    D = Kd *ErrorOne
    
    PID = K*(P + I + D)
    print('P:',P,'I:',I,'D:',D,'PID:',PID)
    return PID

ErrorSum = 0
while True:
    i = 0   #用于给第一次误差赋值
    Cam.ReadImg(0,320,20,150)
    Centre, Sum, Dst = Cam.LineTracking(Cam.Img)
    Cam.ShowImg(Cam.Img)
    Cam.ShowImg(Dst,'Dst')
    Error = Centre[40] - 160
    #print(Sum[40])
    if i == 0:
        i = 1
        ErrorL = 0
    ErrorSum += Error
    PID = PIDControl(0.2,2,0,2,Error,ErrorSum,ErrorL)
    ErrorL = Error
    Cam.Delay(1)
