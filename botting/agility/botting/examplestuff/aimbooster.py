import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def right_click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)#rightclick down
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)#rightclick released

#Color of center: (255, 219, 195)
#120,0,139 goblin
#r == 120 and g == 0 and b == 139 
#255,03,255 tree
#584, 422, 751, 526 SCREENCORDS SO DONT FORGET
while keyboard.is_pressed('q') == False:
    leave = 0
    fullscreen = pyautogui.screenshot(region=(0, 0, 1920, 1080))

    width, height = fullscreen.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = fullscreen.getpixel((x, y))

            if r == 120 and g == 0 and b == 139:
                leave =  1
                right_click(x,y)#+584, y+422)
                print('goblin found')
                time.sleep(.02)
                break

        if leave == 1:
            break