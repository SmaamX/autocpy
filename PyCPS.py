#AUTO and BYPASS
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
print('Start')
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
    h = 0
    while True:
        while ip('v'): #Your hotkey for start
            p = ri(1,22)
            if p == 1:
                coold = grandom(2,3,4,5)
                coold = coold * 10 ** -1
                sl(coold)
            a = grandom(21,90,91,189)
            g = grandom(12,29,30,101)
            if a > h and not a-g <= 0:
                a = a-g
            elif a-g <= 0:
                a = g-a
            else:
                a = a+g
            h = a
            a = a * 10 ** -3
            sl(a)
            pyautogui.leftClick()
        if ip('y'): #Your hotkey for stop
            print ('Stop')
            break
except KeyboardInterrupt:
    print ('Force stop')
