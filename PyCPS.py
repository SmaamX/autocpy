#AutoClicker (unrecognizable)
try:
    import pyautogui
except ModuleNotFoundError:
    print ('pip install pyautogui')
try:
    from keyboard import is_pressed as ip
except ModuleNotFoundError:
    print ('pip install keyboard')
from time import sleep as sl
from random import randint as ri
print('By SmaamX')
pyautogui.PAUSE = 0
try:
    while True:
        while ip('v'):
            cd = ri(4,13)
            if cd == 4:
                df = ri(1,4)
                df = df * 10 ** -1
                sl(df)
            r1 = ri(22,91)
            ri2 = ri(89,192)
            r = ri(r1,ri2)
            r = r * 10 ** -3
            sl(r)
            pyautogui.leftClick()
        if ip('y'):
            print ('exit')
            break
except KeyboardInterrupt:
    print ('Force exit')
