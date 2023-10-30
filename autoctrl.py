# Minecraft AutoRun
import threading
import keyboard
sr=1
def ctrlrun():
    keyboard.press('ctrl')
keyboard.add_hotkey('w',ctrlrun)
fixkey('w','a',ctrlrun)
fixkey('w','d',ctrlrun)
def keyb():
    keyboard.wait()
thread = threading.Thread(target=keyb)
thread.start()
AutoCS()