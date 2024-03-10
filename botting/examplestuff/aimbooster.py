import pyautogui
import time
import keyboard
import random
import win32api, win32con
from stuff import *


def right_click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)#rightclick down
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)#rightclick released

inventory=(1460, 765, 128, 210)
red=(255,0,0)
green=(19,255,0)

def findobj(objsRGBVal, screen=(0,0,1920,1080)):
        flag=0
        width=screen[0]+screen[2]
        height=screen[1]+screen[3]
        for y in range(screen[1], height, 5):
            for x in range(screen[0], width, 5):
                rgb = pyautogui.pixel(x,y)
                if rgb[0] == objsRGBVal[0] and rgb[1] == objsRGBVal[1] and rgb[2] == objsRGBVal[2]:
                    flag = 1
                    new_x= x
                    new_y= y
                    break
                            
            if flag == 1:
                    return new_x,new_y           
class Bag:
    def __init__(self,bagindex=[], screen=(1460, 765, 128, 210),delta_x=43,delta_y=35):
        self.delta_x=delta_x
        self.delta_y=delta_y
        self.bagindex=bagindex
        
        width=screen[0]+screen[2]
        height=screen[1]+screen[3]
        
        for y in range(770, height+delta_y, delta_y):
            for x in range(1460, width+delta_x, delta_x):
                bagindex.append((x,y))
    
    def eatfood(self, objsRGBVal=(0,0,255)):
        for i in self.bagindex:
            if pyautogui.pixel(i[0],i[1]) == objsRGBVal:
                Randomize((i[0]-1,i[0]+1,i[1]-1,i[1]+1)).randleft()
                break
    

inventory=Bag()
eatshark=inventory.eatfood(red)
eatkarambwan=inventory.eatfood(green)

