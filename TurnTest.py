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

L= GPIO_RPi.L298N(18,16,35,37,33,31)
L.Stop()

def readWord(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

# 将读取到的数据转换为原码 (有符号数本身是采用补码方式存储的)
def readWordReal(adr):
    val = readWord(adr)
    x = 0xffff
    # 首位为1 表示是负数
    if (val >= 0x8000):
        # 求原码
        return -((x - val)+1)
    else:
        return val

def GetZ():
    gyroZ = readWordReal(0x47)/131
    if abs(gyroZ) <= 1.5:  #防止零飘
        gyroZ = 0
    else:
        pass  #左边为正右边为负数
    return gyroZ

def TurnLeft(TurnTime = 7800):
    Flag = 0
    time.sleep(0.5) #给陀螺仪修正时间
    while True:
        Z = GetZ()
        Flag += Z
        if Flag >= TurnTime:
            break
        else:
            L.TurnLeft(40,40)
        time.sleep(0.01)
    L.Stop()
    print(Flag)
    print('Trun done')
    
TurnLeft()