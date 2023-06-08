#PyCPS Beta
print ('Loading...')
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
pyautogui.PAUSE = 0
print('Start')

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

    def fixkey (x,y):
        keyboard.add_hotkey(x +'+'+ y, on_start_pressed)
        keyboard.add_hotkey(y +'+'+ x, on_start_pressed)

    def fixkey3 (x,y,z):
        keyboard.add_hotkey(x +'+'+ y +'+'+ z, on_start_pressed)
        keyboard.add_hotkey(z+'+'+ x +'+'+ y, on_start_pressed)
        keyboard.add_hotkey(x +'+'+ z +'+'+ y, on_start_pressed)
        keyboard.add_hotkey(y +'+'+ x +'+'+ z, on_start_pressed)
        keyboard.add_hotkey(z +'+'+ y +'+'+ x, on_start_pressed)
        keyboard.add_hotkey(y +'+'+ z +'+'+ x, on_start_pressed)

    def fixkey4 (x,y,z,s):
        keyboard.add_hotkey(x +'+'+ y +'+'+ z +'+'+ s, on_start_pressed)
        keyboard.add_hotkey(x +'+'+ y +'+'+ s +'+'+ z, on_start_pressed)
        keyboard.add_hotkey(x +'+'+ s +'+'+ y +'+'+ z, on_start_pressed)
        keyboard.add_hotkey(s +'+'+ x +'+'+ y +'+'+ z, on_start_pressed)
        keyboard.add_hotkey(z +'+'+ x +'+'+ y +'+'+ s, on_start_pressed)
        keyboard.add_hotkey(z +'+'+ x +'+'+ s +'+'+ y, on_start_pressed)
        keyboard.add_hotkey(z +'+'+ s +'+'+ x +'+'+ y, on_start_pressed)
        keyboard.add_hotkey(s +'+'+ z +'+'+ x +'+'+ y, on_start_pressed)
        keyboard.add_hotkey(x +'+'+ z +'+'+ y +'+'+ s, on_start_pressed)
        keyboard.add_hotkey(x +'+'+ z +'+'+ s +'+'+ y, on_start_pressed)
        keyboard.add_hotkey(x +'+'+ s +'+'+ z +'+'+ y, on_start_pressed)
        keyboard.add_hotkey(s +'+'+ x +'+'+ z +'+'+ y, on_start_pressed)
        keyboard.add_hotkey(y +'+'+ x +'+'+ z +'+'+ s, on_start_pressed)
        keyboard.add_hotkey(y +'+'+ x +'+'+ s +'+'+ z, on_start_pressed)
        keyboard.add_hotkey(y +'+'+ s +'+'+ x +'+'+ z, on_start_pressed)
        keyboard.add_hotkey(s +'+'+ y +'+'+ x +'+'+ z, on_start_pressed)
        keyboard.add_hotkey(z +'+'+ y +'+'+ x +'+'+ s, on_start_pressed)
        keyboard.add_hotkey(z +'+'+ y +'+'+ s +'+'+ x, on_start_pressed)
        keyboard.add_hotkey(z +'+'+ s +'+'+ y +'+'+ x, on_start_pressed)
        keyboard.add_hotkey(s +'+'+ z +'+'+ y +'+'+ x, on_start_pressed)
        keyboard.add_hotkey(y +'+'+ z +'+'+ x +'+'+ s, on_start_pressed)
        keyboard.add_hotkey(y +'+'+ z +'+'+ s +'+'+ x, on_start_pressed)
        keyboard.add_hotkey(y +'+'+ s +'+'+ z +'+'+ x, on_start_pressed)
        keyboard.add_hotkey(s +'+'+ y +'+'+ z +'+'+ x, on_start_pressed)

    def fixkey5(x,r,s):
        keyboard.add_hotkey(x +'+'+ r +'+'+ s, on_start_pressed)
        keyboard.add_hotkey(s+'+'+ x +'+'+ r, on_start_pressed)
        keyboard.add_hotkey(x +'+'+ s +'+'+ r, on_start_pressed)
        keyboard.add_hotkey(r +'+'+ x +'+'+ s, on_start_pressed)
        keyboard.add_hotkey(s +'+'+ r +'+'+ x, on_start_pressed)
        keyboard.add_hotkey(r +'+'+ s +'+'+ x, on_start_pressed)
    
    def mkey(x,y,z,a,r,s):
        fixkey (x,r)
        fixkey (y,r)
        fixkey (a,r)
        fixkey (z,r)
        fixkey3 (x,y,r)
        fixkey3 (x,a,r)
        fixkey3 (x,z,r)
        fixkey3 (y,z,r)
        fixkey3 (y,a,r)
        fixkey3 (a,z,r)
        fixkey5 (x,r,s)
        fixkey5 (y,r,s)
        fixkey5 (z,r,s)
        fixkey5 (a,r,s)
        fixkey4 (x,y,r,s)
        fixkey4 (x,a,r,s)
        fixkey4 (x,z,r,s)
        fixkey4 (y,z,r,s)
        fixkey4 (y,a,r,s)
        fixkey4 (a,z,r,s)

    mkey('w','a','s','d','r','space')
    keyboard.add_hotkey('r', on_start_pressed)
    keyboard.add_hotkey('y', on_stop_pressed)
    keyboard.wait()
except KeyboardInterrupt:
    print ('Force stop')