#PyCPS Beta
import tkinter as tk
from sys import argv;from os import system as sys
try:
    if __name__ == '__main__':
        import tempfile
        import string
        import random
        TMP = tempfile.gettempdir() + "\\" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        import psutil
        import os
        import ctypes
        sys('cls')
        print('STemp:',TMP)
        length = random.randint(9, 10)
        proc = ''.join(random.choices(string.ascii_lowercase, k=length))
        argv[0]= proc
        print('Spoofed:',proc)
        pid = os.getpid()
        print('PID:',pid)
        try:
            print('[FucHide]')
            han = ctypes.windll.kernel32.GetModuleHandleW(None)
            ctypes.windll.kernel32.SetProcessWorkingSetSizeEx(han,-1,-1,0x100)
            spoof2 = ''.join(random.choices(string.ascii_lowercase, k=length))
            ctypes.windll.kernel32.SetConsoleTitleW(spoof2);print('ConsoleTitle:',spoof2)
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
            p = psutil.Process(pid)
            p.nice(psutil.HIGH_PRIORITY_CLASS)
            import ctypes
#
            PROCESS_ALL_ACCESS = 0x1F0FFF
            PROCESS_QUERY_INFORMATION = 0x0400
            PROCESS_VM_READ = 0x0010
            han3 = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, ctypes.windll.kernel32.GetCurrentProcessId())
            path = ctypes.create_unicode_buffer(1024)
            ctypes.windll.psapi.GetModuleFileNameExW(han3, 0, path, ctypes.sizeof(path))
            ctypes.windll.ntdll.NtSetInformationProcess(han3, 0x1D, path, ctypes.sizeof(path))
            ctypes.windll.kernel32.CloseHandle(han3)
        except: print('[un_FucHide]')
except: print('un_spoof')
def color(x,C):
    try:
        from colorama import Fore as fo
        if C==1:print(fo.RED+x)
        if C==2:print(fo.GREEN+x)
        if C==3:print(fo.BLUE+x)
    except ModuleNotFoundError:
        print(x)
def AutoCS():
    global LBM
    global h1
    global leftCL
    global rightCL
    global h2
    sys('cls')
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
#
    color('START',3)
    color('R.I.P Technoblade',2)
    LBM = input('Jitter (Y/N):')
    LBM = True if any(x.lower() in ['y', 'yes'] for x in LBM) else False
    if LBM == True: color('ON',2)
    else: color('OFF',1)
    sl(1)
#
    def randx(x,y,z,ax,x0,y0,z0,a0,x1,y1,z1,a1,x2,y2,z2,a2,x3,y3,z3,a3,x4,y4,z4,a4,x5,y5,z5,a5,h2):
        global LBM
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
            global leftCL
            global h1
            global LBM
            cooldown(40,50)
            p = randx(2,5,6,8,1,2,3,4,2,3,4,5,12,31,32,191,4,10,11,55,2,10,20,21,9,11,25,26,h1)
                                          #                    #
            h1 = p
            p = p * 10 ** -3
            if LBM==True: st1 = std(0,1,70)
            else: st1 = std(0,1,60)
            #color('STD:'+str(st1),2)
            sl(p)
            if keyboard.is_pressed(leftCL):
                pyautogui.mouseDown(button='left')
                #sl(st1)
                pyautogui.mouseUp(button='left')
#
        def start2():
            global rightCL
            global h2
            global LBM
            cooldown(40,50)
            p = randx(2,5,6,8,1,2,3,4,2,3,4,5,12,31,32,191,3,12,25,26,7,21,22,24,12,24,25,26,h2)
                                          #                    #
            h2 = p
            p = p * 10 ** -3
            if LBM==True: st = std(0,1,50)
            else: st = std(0,1,40)
            sl(p)
            if keyboard.is_pressed(rightCL):
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
                if keyboard.is_pressed(skey):
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
        sys('cls')
        while True:
            color('KeyMap editor',2)
            try:keymap = int(input('1.Minecraft\n2.Custom\n'))
            except: keymap = 0
            if keymap == 1:
                sys('cls')
                print('Minecraft')
                leftCL = 'r';rightCL = 'f'
                tomkey ('w','a','s','d','r','space','ctrl','shift',on_start_pressed)
                tomkey ('w','a','s','d','f','space','ctrl','shift',on_start2_pressed)
                keyboard.add_hotkey('r',on_start_pressed);keyboard.add_hotkey('f',on_start2_pressed);skey = 'ctrl+y';keyboard.add_hotkey('ctrl+y',on_stop_pressed)#for stop - skey = 'x';keyboard.add_hotkey('x',on_stop_pressed)
                break
            elif keymap == 2:
                sys('cls')
                #0 and ckeymapR just for r and f key if 1 just 1 key = [0]
                def godkey(ckeymap):
                    global leftCL
                    global rightCL
                    global skey
                    ERR = False
                    try:
                        while True:ckeymap.remove(',')
                    except: pass
                    try:
                        ckeymapA = len(ckeymap)
                        if ckeymapA > 1:ckeymapS = ckeymap[-1];ckeymap.remove(ckeymap[-1]);print ('stop key=','Ctrl'+'+'+ckeymapS);skey = ckeymapS;keyboard.add_hotkey('ctrl'+'+'+ckeymapS, on_stop_pressed)
                        print('Keys:',ckeymap);ckeymapN = len(ckeymap)
                        if ckeymapN == 1:keyboard.add_hotkey(ckeymap[0], on_start_pressed)
                        elif ckeymapN == 2:leftCL = ckeymap[0];rightCL = ckeymap[1];tomkey (ckeymap[0],'F6','F7','F8','F9','F10','F11','F12',on_start_pressed);tomkey (ckeymap[1],'F6','F7','F8','F9','F10','F12','F11',on_start2_pressed);keyboard.add_hotkey(ckeymap[0], on_start_pressed);keyboard.add_hotkey(ckeymap[1], on_start2_pressed)
                        elif ckeymapN == 3:leftCL = ckeymap[0];rightCL = ckeymap[1];tomkey (ckeymap[0],ckeymap[2],'F7','F8','F9','F10','F11','F12',on_start_pressed);tomkey (ckeymap[1],ckeymap[2],'F7','F8','F9','F10','F12','F11',on_start2_pressed);keyboard.add_hotkey(ckeymap[0], on_start_pressed);keyboard.add_hotkey(ckeymap[1], on_start2_pressed)
                        elif ckeymapN == 4:leftCL = ckeymap[0];rightCL = ckeymap[1];tomkey (ckeymap[0],ckeymap[2],ckeymap[3],'F8','F9','F10','F11','F12',on_start_pressed);tomkey (ckeymap[1],ckeymap[2],ckeymap[3],'F8','F9','F10','F12','F11',on_start2_pressed);keyboard.add_hotkey(ckeymap[0], on_start_pressed);keyboard.add_hotkey(ckeymap[1], on_start2_pressed)
                        elif ckeymapN == 5:leftCL = ckeymap[0];rightCL = ckeymap[1];tomkey (ckeymap[0],ckeymap[2],ckeymap[3],ckeymap[4],'F9','F10','F11','F12',on_start_pressed);tomkey (ckeymap[1],ckeymap[2],ckeymap[3],ckeymap[4],'F9','F10','F12','F11',on_start2_pressed);keyboard.add_hotkey(ckeymap[0], on_start_pressed);keyboard.add_hotkey(ckeymap[1], on_start2_pressed)
                        elif ckeymapN == 6:leftCL = ckeymap[0];rightCL = ckeymap[1];tomkey (ckeymap[0],ckeymap[2],ckeymap[3],ckeymap[4],ckeymap[5],'F10','F11','F12',on_start_pressed);tomkey (ckeymap[1],ckeymap[2],ckeymap[3],ckeymap[4],ckeymap[5],'F10','F12','F11',on_start2_pressed);keyboard.add_hotkey(ckeymap[0], on_start_pressed);keyboard.add_hotkey(ckeymap[1], on_start2_pressed)
                        elif ckeymapN == 7:leftCL = ckeymap[0];rightCL = ckeymap[1];tomkey (ckeymap[0],ckeymap[2],ckeymap[3],ckeymap[4],ckeymap[5],ckeymap[6],'F11','F12',on_start_pressed);tomkey (ckeymap[1],ckeymap[2],ckeymap[3],ckeymap[4],ckeymap[5],ckeymap[6],'F12','F11',on_start2_pressed);keyboard.add_hotkey(ckeymap[0], on_start_pressed);keyboard.add_hotkey(ckeymap[1], on_start2_pressed)
                        elif ckeymapN == 8:leftCL = ckeymap[0];rightCL = ckeymap[1];tomkey (ckeymap[0],ckeymap[2],ckeymap[3],ckeymap[4],ckeymap[5],ckeymap[6],ckeymap[7],'F11',on_start_pressed);tomkey (ckeymap[1],ckeymap[2],ckeymap[3],ckeymap[4],ckeymap[5],ckeymap[6],ckeymap[7],'F11',on_start2_pressed);keyboard.add_hotkey(ckeymap[0], on_start_pressed);keyboard.add_hotkey(ckeymap[1], on_start2_pressed)
                        elif ckeymapN > 8:color('Error/Above',1);ERR=True
                        elif ckeymapN < 1:color('Error/Below',1);ERR=True
                        elif ckeymapN == 0:color('Error/Zero',1);ERR=True
                    except: print('E/KNF')
                    return ERR
                ckeymap = list(input('Give custom KeyMap {1,9} keys\nexample ~ r,f,a,w,d,end ~~ (r) = hotkey for r click and (f) for l\n0 = r and 1 = f and end = ctrl + (stop key)\n'));ERR = godkey(ckeymap)
                if ERR == False:break
                elif ERR == True:pass
            else: color('Bad input',1)
        keyboard.wait()
    except KeyboardInterrupt:
        print ('ForceStop')
#################TermPy_conf#################
def TermPyS():
    sys('cls');color('TermPy 1.2',2);import code;import ctypes;import subprocess;import tempfile;import random;import string
    class MgiConsole(code.InteractiveConsole):
        TMP2 = tempfile.gettempdir() + "\\" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        print('STemp2:',TMP2)
        import code;import ctypes;import subprocess;import tempfile;import random;import string
    console = MgiConsole()
    console.interact()
#GUI
import tkinter as tk
import random
root = tk.Tk()
def rword():
    return ''.join(random.choice(string.ascii_letters) for i in range(7))
root.title(rword())
#
def AutoC():
    root.destroy()
    AutoCS()
def TermPy():
    root.destroy()
    TermPyS()
def Exit():
    root.destroy()
    exit()
#
AutoC = tk.Button(root, text="AutoC", command=AutoC)
AutoC.pack()
TermPy = tk.Button(root, text="TermPy", command=TermPy)
TermPy.pack()
Exit = tk.Button(root, text="Exit", command=Exit)
Exit.pack()
root.mainloop()