#coding:utf-8

import smbus
import math
import time

# 电源控制寄存器地址
power_regist = 0x6b

# I2C模块初始化
bus = smbus.SMBus(1)
# 外接I2C设备的地址
address = 0x68

# 封装一些读取数据的功能函数

# 读取一个字长度的数据(16位)
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

# 已知加速度求角度值
def dist(a, b):
    return math.sqrt((a*a)+(b*b))

def getRotationX(x, y, z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def getRotationY(x, y, z):
    radians = math.atan2(x, dist(y,z))
    return math.degrees(radians)

# 设置电源模式
bus.write_byte_data(address, power_regist, 0)


while True:
    time.sleep(0.5)
    print("螺旋仪数据-----------")
    gyroX = readWordReal(0x43)
    gyroY = readWordReal(0x45)
    gyroZ = readWordReal(0x47)

    print("X轴陀螺仪原始数据：", gyroX, "X轴每秒旋转度数：", gyroX/131)
    print("Y轴陀螺仪原始数据：", gyroY, "Y轴每秒旋转度数：", gyroY/131)
    print("Z轴陀螺仪原始数据：", gyroZ, "Z轴每秒旋转度数：", gyroZ/131)

    print("加速度数据----------")
    accelX = readWordReal(0x3b)
    accelY = readWordReal(0x3d)
    accelZ = readWordReal(0x3f)

    print("X轴加速度原始数据：", accelX, "X轴加速度：", accelX/16384)
    print("Y轴加速度原始数据：", accelY, "Y轴加速度：", accelY/16384)
    print("Z轴加速度原始数据：", accelZ, "Z轴加速度：", accelZ/16384)

    print("摄氏温度数据--------")
    temp = readWordReal(0x41)
    print("温度原始数据：", temp, "摄氏度：", temp/340 + 36.53)

    print("旋转家角度数据-------")
    print("X轴旋转度数：", getRotationX(accelX/16384, accelY/16384, accelZ/16384))
    print("Y轴旋转度数：", getRotationX(accelX/16384, accelY/16384, accelZ/16384))