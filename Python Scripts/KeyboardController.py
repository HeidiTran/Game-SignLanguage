from pynput.keyboard import Key, Controller
import time 
import keyboard

controller = Controller()
counter = 0

while True:
    if keyboard.is_pressed('j'):
        controller.press('a')
        controller.release('a')
        counter += 1
        if counter > 1:
            counter = 0 
            continue
    if keyboard.is_pressed('k'):
        controller.press('s')
        controller.release('s')
        continue
    if keyboard.is_pressed('l'):
        controller.press('d')
        controller.release('d')
        continue
    if keyboard.is_pressed('i'):
        controller.press('w')
        controller.release('w')
        continue
    if keyboard.is_pressed('q'):
        break
    else:
        pass