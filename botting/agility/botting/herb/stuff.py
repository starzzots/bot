import pyautogui as pg
import time
import random
import win32con, win32api
import keyboard
from win32gui import FindWindow, GetWindowRect

bagcords= [(1451,1465,763,771),(1496,1506,760,769),(1536,1548,760,769),(1576,1588,760,769),
           (1451,1465,797,807),(1496,1504,797,807),(1536,1545,797,805),(1576,1587,797,807),
           (1451,1465,822,832),(1496,1504,822,832),(1536,1545,822,832),(1576,1587,822,832),
           (1451,1465,847,857),(1496,1504,847,857),(1536,1545,847,857),(1576,1587,847,857),
           (1451,1465,872,882),(1496,1504,872,882),(1536,1545,872,882),(1576,1587,872,882),
           (1451,1465,897,907),(1496,1504,897,907),(1536,1545,897,907),(1576,1587,897,907),
           (1451,1465,922,932),(1496,1504,922,932),(1536,1545,922,932),(1576,1587,922,932)]


class Randomize():
    def __init__(self,minMaxs):
        self.minMaxs = [minMaxs] # (min_x, max_x, min_y, max_y)
        self.x_min = minMaxs[0]
        self.x_max = minMaxs[1]
        self.y_min = minMaxs[2]
        self.y_max = minMaxs[3]
        self.random_pix_move_y = random.randrange(25,27,1)
        self.random_pix_move_x = random.randrange(-40,40,1)

        self.random_multi = random.randrange(30,50,1)/100

        self.random_sleep= random.randrange(30,40,1)/100
        self.random_sleep2= random.randrange(10,30,1)/100
        self.random_sleep3= random.randrange(30,50,1)/1000
        self.random_long_sleep = random.randrange(20,50,1)/100
        self.new_x = random.randrange(self.x_min, self.x_max+1)
        self.new_y = random.randrange(self.y_min, self.y_max+1)

    def shiftclick(self):
        keyboard.press('shift')
        pg.moveTo(self.new_x,self.new_y, duration=.25)
        time.sleep(.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(.08)
        keyboard.release('shift')

    def move(self):
        pg.moveTo(self.new_x,self.new_y, duration=self.random_sleep2)

    
    def randleftspeed(self):
        pg.moveTo(self.new_x,self.new_y, duration=.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(.02)
    
    
    def randleft(self):
        pg.moveTo(self.new_x,self.new_y, duration=.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(.03)
    
    
    def dragmove(self,x,y):
        pg.moveTo(self.new_x,self.new_y, duration=.3)
        time.sleep(self.random_sleep)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        pg.moveTo(x, y, duration=.6)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(self.random_sleep3)

def findobj(objsRGBVal):
        flag=0
        
        screen=pg.screenshot(region=(0,0,1920,1080))
        time.sleep(.3)
        width, height = screen.size
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                rgb = screen.getpixel((x, y))
                if rgb==objsRGBVal:
                    flag = 1
                    new_x= x
                    new_y= y
                    time.sleep(0.05)
                    break
                            
            if flag == 1:
                    return new_x,new_y
            
     