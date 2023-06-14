#PyCPS Beta
try:
    from os import system as sys
    sys('clear')
    sys('cls')
except: pass
try:
    import pyautogui
except ModuleNotFoundError:
    print ('pip install pyautogui')
    exit()
try:
    import keyboard
    from keyboard import is_pressed as ip
except ModuleNotFoundError:
    print ('pip install keyboard')
    exit()
from time import sleep as sl
from random import randint as ri
pyautogui.PAUSE = 0
def color(x,C):
    try:
        from colorama import Fore as fo
        if C==1:print(fo.RED+x)
        if C==2:print(fo.GREEN+x)
        if C==3:print(fo.BLUE+x)
    except ModuleNotFoundError:
        print(x)
#
color('START',3)
color('R.I.P Technoblade',2)
LBM = input('Jitter (Y/N):')
LBM = True if any(x.lower() in ['y', 'yes'] for x in LBM) else False
if LBM == True: color('ON',2)
else: color('OFF',1)
#
def randx(x,y,z,ax,x0,y0,z0,a0,x1,y1,z1,a1,x2,y2,z2,a2,x3,y3,z3,a3,x4,y4,z4,a4,x5,y5,z5,a5,h2):
    if LBM == False:
        a = grandom(x2,y2,z2,a2)
        g = grandom(x3,y3,z3,a3)
    elif LBM == True:
        a = grandom(x4,y4,z4,a4)
        g = grandom(x5,y5,z5,a5)
    m = grandom(x,y,z,ax)
    m1 = grandom(x0,y0,z0,a0)
    m2 = grandom(x1,y1,z1,a1)
    if a > h2 and not a/m2-g+m-m1 <= 0:
        a = a/m2-g+m-m1
    elif a-g <= 0:
        a = (g-a+m)*(m1/m2)+m2
    elif a < h2 and not a/m2-g-m+(m1/2) <= 0:
        a = a/m2-g-m+(m1/2)
    else: a = (a+g-m)*(m1/m2)+m2
    return a
#
def std(x,y,z):
    std = ri (0,z)
    x1 = ri (x,y)
    x2 = ri (0,9)
    x3 = ri (0,9)
    if std == 1: x1 = x1 * 10 ** -1;x1=x1+(x2*10**-2)+(x3*10**-3)
    elif std == 0: x1 = x1 * 10 ** -2;x1=x1+(x3*10**-3)
    else:x1 = x1 * 10 ** -3
    x = x1
    color('STD:'+str(std),1)
    return x
#
def cooldown(b,d):
    global LBM
    pt1 = False; pt2 = False; pt3 = False; pt4 = False
    coold = 0
    if LBM == True:
        p = ri(1,b)
    elif LBM == False:
        p = ri(1,d)
    if p == 1:
        coold = grandom(1,2,3,4)
        coold = coold * 10 ** -1
        pt1 = True
    elif p == 20:
        coold = grandom(1,3,4,5)
        coold = coold * 10 ** -2
        pt2 = True
    elif p == 25:
        coold = grandom(1,3,4,5)
        coold = coold * 10 ** -3
    elif p == 30:
        coold = grandom(1,2,3,4)
        coold = coold * 10 ** -2
        pt3 = True
    elif p == 35:
        coold = grandom(1,2,3,4)
        coold = coold * 10 ** -3
    elif p == 40:
        coold = grandom(1,3,4,5)
        coold = coold * 10 ** -1
        pt4 = True
    if pt1 or pt2 or pt3 or pt4 == True:
        if pt1 == True: sp1 = ri(1,9);sp1 = sp1 * (10 ** -2);sp2 = ri(1,9);sp2 = sp2 * (10 ** -3);coold = coold + sp1 + sp2
        if pt2 == True: sp2 = ri(1,9);sp2 = sp2 * (10 ** -3);coold = coold + sp2
        if pt3 == True: sp2 = ri(1,9);sp2 = sp2 * (10 ** -3);coold = coold + sp2
        if pt4 == True: sp1 = ri(1,9);sp1 = sp1 * (10 ** -2);sp2 = ri(1,9);sp2 = sp2 * (10 ** -3);coold = coold + sp1 + sp2
    color('CoolDown:'+str(coold),2)
    sl(coold)
#
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
    h1 = 0
    h2 = 0
    def start():
        global h1
        global LBM
        cooldown(50,60)
        p = randx(2,5,6,8,1,2,3,4,2,3,4,5,12,21,22,83,4,10,11,55,2,10,20,21,9,11,25,26,h1)
                                          #                   #
        h1 = p
        p = p * 10 ** -3
        if LBM==True: st1 = std(0,1,70)
        else: st1 = std(0,1,60)
        #color('STD:'+str(st1),2)
        sl(p)
        if keyboard.is_pressed('r'):
            pyautogui.mouseDown(button='left')
            #sl(st1)
            pyautogui.mouseUp(button='left')
#
    def start2():
        global h2
        global LBM
        cooldown(50,60)
        p = randx(2,5,6,8,1,2,3,4,2,3,4,5,2,21,22,81,3,12,25,26,7,21,22,24,12,24,25,26,h2)
                                          #                   #
        h2 = p
        p = p * 10 ** -3
        if LBM==True: st = std(0,1,70)
        else: st = std(0,1,60)
        sl(p)
        if keyboard.is_pressed('f'):
            pyautogui.mouseDown(button='right')
            sl(st)
            pyautogui.mouseUp(button='right')
    def on_start_pressed():
        start()
    def on_start2_pressed():
        start2()
    def on_stop_pressed():
        print('Stop')
        sl (1)
        while True:
            if keyboard.is_pressed('y'):
                print('Restart')
                sl (1)
                break
    def fixkey (x,y,rt):
        keyboard.add_hotkey(x +'+'+ y, rt)
        keyboard.add_hotkey(y +'+'+ x, rt)
#
    def fixkey3 (x,y,z,rt):
        keyboard.add_hotkey(x +'+'+ y +'+'+ z, rt)
        keyboard.add_hotkey(z+'+'+ x +'+'+ y, rt)
        keyboard.add_hotkey(x +'+'+ z +'+'+ y, rt)
        keyboard.add_hotkey(y +'+'+ x +'+'+ z, rt)
        keyboard.add_hotkey(z +'+'+ y +'+'+ x, rt)
        keyboard.add_hotkey(y +'+'+ z +'+'+ x, rt)
#
    def fixkey4 (x,y,z,s,rt):
        keyboard.add_hotkey(x +'+'+ y +'+'+ z +'+'+ s, rt)
        keyboard.add_hotkey(x +'+'+ y +'+'+ s +'+'+ z, rt)
        keyboard.add_hotkey(x +'+'+ s +'+'+ y +'+'+ z, rt)
        keyboard.add_hotkey(s +'+'+ x +'+'+ y +'+'+ z, rt)
        keyboard.add_hotkey(z +'+'+ x +'+'+ y +'+'+ s, rt)
        keyboard.add_hotkey(z +'+'+ x +'+'+ s +'+'+ y, rt)
        keyboard.add_hotkey(z +'+'+ s +'+'+ x +'+'+ y, rt)
        keyboard.add_hotkey(s +'+'+ z +'+'+ x +'+'+ y, rt)
        keyboard.add_hotkey(x +'+'+ z +'+'+ y +'+'+ s, rt)
        keyboard.add_hotkey(x +'+'+ z +'+'+ s +'+'+ y, rt)
        keyboard.add_hotkey(x +'+'+ s +'+'+ z +'+'+ y, rt)
        keyboard.add_hotkey(s +'+'+ x +'+'+ z +'+'+ y, rt)
        keyboard.add_hotkey(y +'+'+ x +'+'+ z +'+'+ s, rt)
        keyboard.add_hotkey(y +'+'+ x +'+'+ s +'+'+ z, rt)
        keyboard.add_hotkey(y +'+'+ s +'+'+ x +'+'+ z, rt)
        keyboard.add_hotkey(s +'+'+ y +'+'+ x +'+'+ z, rt)
        keyboard.add_hotkey(z +'+'+ y +'+'+ x +'+'+ s, rt)
        keyboard.add_hotkey(z +'+'+ y +'+'+ s +'+'+ x, rt)
        keyboard.add_hotkey(z +'+'+ s +'+'+ y +'+'+ x, rt)
        keyboard.add_hotkey(s +'+'+ z +'+'+ y +'+'+ x, rt)
        keyboard.add_hotkey(y +'+'+ z +'+'+ x +'+'+ s, rt)
        keyboard.add_hotkey(y +'+'+ z +'+'+ s +'+'+ x, rt)
        keyboard.add_hotkey(y +'+'+ s +'+'+ z +'+'+ x, rt)
        keyboard.add_hotkey(s +'+'+ y +'+'+ z +'+'+ x, rt)
#
    def fixkey5(x,r,s,rt):
        keyboard.add_hotkey(x +'+'+ r +'+'+ s, rt)
        keyboard.add_hotkey(s+'+'+ x +'+'+ r, rt)
        keyboard.add_hotkey(x +'+'+ s +'+'+ r, rt)
        keyboard.add_hotkey(r +'+'+ x +'+'+ s, rt)
        keyboard.add_hotkey(s +'+'+ r +'+'+ x, rt)
        keyboard.add_hotkey(r +'+'+ s +'+'+ x, rt)
#  
    def mkey(x,y,z,a,r,s,rt):
        fixkey (x,r,rt)
        fixkey (y,r,rt)
        fixkey (a,r,rt)
        fixkey (z,r,rt)
        fixkey (s,r,rt)
        fixkey3 (x,y,r,rt)
        fixkey3 (x,a,r,rt)
        fixkey3 (x,z,r,rt)
        fixkey3 (y,z,r,rt)
        fixkey3 (y,a,r,rt)
        fixkey3 (a,z,r,rt)
        fixkey5 (x,r,s,rt)
        fixkey5 (y,r,s,rt)
        fixkey5 (z,r,s,rt)
        fixkey5 (a,r,s,rt)
        fixkey4 (x,y,r,s,rt)
        fixkey4 (x,a,r,s,rt)
        fixkey4 (x,z,r,s,rt)
        fixkey4 (y,z,r,s,rt)
        fixkey4 (y,a,r,s,rt)
        fixkey4 (a,z,r,s,rt)
    def tomkey (x,y,z,a,r,s,c,sh,rt):
        mkey(x,y,z,a,r,s,rt)
        mkey(x,y,z,c,r,s,rt)
        mkey(x,y,z,a,r,c,rt)
        mkey(x,y,z,sh,r,s,rt)
        mkey(x,y,z,a,r,sh,rt)
    tomkey ('w','a','s','d','r','space','ctrl','shift',on_start_pressed)
    tomkey ('w','a','s','d','f','space','ctrl','shift',on_start2_pressed)
    keyboard.add_hotkey('r', on_start_pressed)
    keyboard.add_hotkey('f', on_start2_pressed)
    keyboard.add_hotkey('ctrl+y', on_stop_pressed)
    keyboard.wait()
except KeyboardInterrupt:
    print ('Force stop')