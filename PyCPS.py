#PyCPS Beta
try:
    import pyautogui
except ModuleNotFoundError:
    print ('pip install pyautogui')
try:
    import keyboard
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
    def start():
        global h
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
        else: a = a+g
        h = a
        a = a * 10 ** -3
        sl(a)
        pyautogui.leftClick()
    def on_start_pressed():
        start()
    def on_stop_pressed():
        print('Stop')
        exit()
    keyboard.add_hotkey('v', on_start_pressed)  
    keyboard.add_hotkey('y', on_stop_pressed)
    keyboard.wait()
except KeyboardInterrupt:
    print ('Force stop')
