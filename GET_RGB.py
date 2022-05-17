from YYJ import Vision

Cam =  Vision.Camera(0, 320, 240)
while True:
    Cam.ReadImg(0,320,0,150)
    Cam.ShowImg(Cam.Img)
    print(Cam.Img[80,160])
    array = Cam.Img[80,160]
    R = array[2]
    G = array[1]
    B = array[0]
    if R >= 100 and G <= 100 and B <= 100:
        print('红色')
    elif R <= 100 and G >= 100 and B >= 100:
        print('浅绿色')
    elif R <= 100 and G >= 70 and B <= 100:
        print('绿色')
    elif R <= 100 and G <= 100 and B >= 70:
        print('蓝色')
    else:
        print('无效颜色')
    Cam.Delay(1)