import sys
import os

Path = '/home/pi/Desktop/F_NEW_Version/Drug/'   #存放录音文件的位置
#os.system('mplayer %s' % '/home/pi/Desktop/F_NEW_Version/Drug/1.aac')
def PlaySound(Name):
    print(Path + Name + 'aac')
    os.system('mplayer %s' % Path + Name + '.aac')

PlaySound('1')