#auto clicker but unrecognizable 90%
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

def grandom(x,y,z,a):
    d = ri(1,2)
    if d == 1:
        r1 = ri(x,y)
        ri2 = ri(z,a)
        r = ri(r1,ri2)
    else:
        r1 = ri(z,a)
        ri2 = ri(x,y)
        r = ri(ri2,r1)
    return r

try:
    while True:
        while ip('v'): #Your hotkey for start
            p = ri(1,20)
            if p == 1:
                coold = grandom(2,3,4,5)
                coold = coold * 10 ** -1
                sl(coold)
            a = grandom(23,91,92,192)
            a = a * 10 ** -3
            sl(a)
            pyautogui.leftClick()
        if ip('y'): #Your hotkey for stop
            print ('exit')
            break
except KeyboardInterrupt:
    print ('Force exit')
