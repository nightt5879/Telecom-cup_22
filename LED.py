from YYJ import GPIO_RPi
from YYJ import Vision

Green = GPIO_RPi.IO(40, 'OUT')
Green.SetPWM(2)
Green.ChangePWM(50)

White = GPIO_RPi.IO(38, 'OUT')
White.SetPWM(2)
White.ChangePWM(50)