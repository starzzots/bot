import pyautogui as pg
import time
import random
import win32con, win32api
from const import *
import keyboard
from win32gui import FindWindow, GetWindowRect

def bonusbloods(topleft):
    Randomize((topleft[0]+1171,topleft[1]+1182,topleft[0]+498,topleft[1]+510)).randleft()#magebook
    time.sleep(.5)
    Randomize((topleft[0]+993,topleft[1]+1005,topleft[0]+560,topleft[1]+570)).randleft()#npc contact
    time.sleep(.5)
    Randomize((topleft[0]+460,topleft[1]+473,topleft[0]+255,topleft[1]+288)).randleft()#Dark Mage contact
    time.sleep(8)
    keyboard.press('space')
    time.sleep(2)
    keyboard.release('space')
    time.sleep(.5)
    keyboard.press('1')
    time.sleep(.2)
    keyboard.release('1')
    time.sleep(.5)
    keyboard.press('space')
    time.sleep(4)
    keyboard.release('space')
    time.sleep(.5)
    keyboard.press('space')
    time.sleep(.5)
    keyboard.release('space')
    time.sleep(.5)
    keyboard.press('space')
    time.sleep(.5)
    keyboard.release('space')
    time.sleep(.5)
    Randomize((topleft[0]+1073,topleft[1]+1086,topleft[0]+498,topleft[1]+516)).randleft()#bag

def bloodstuff(topleft):
    Randomize((topleft[0]+1014,topleft[1]+1021,topleft[0]+548,topleft[1]+557)).randleftspeed()#pouch1 fill
    time.sleep(.1)
    Randomize((topleft[0]+1057,topleft[1]+1066,topleft[0]+546,topleft[1]+558)).randleftspeed()#pouch2 fill
    time.sleep(.1)
    Randomize((topleft[0]+1097,topleft[1]+1108,topleft[0]+546,topleft[1]+561)).randleftspeed()#pouch3 fill
    time.sleep(.1)
    Randomize((topleft[0]+575,topleft[1]+584,topleft[0]+417,topleft[1]+425)).randleft()#bloodalter
    time.sleep(.1)
    Randomize((topleft[0]+1140,topleft[1]+1151,topleft[0]+548,topleft[1]+560)).randleftspeed()#pouch4 fill
    time.sleep(.5)
    Randomize((topleft[0]+575,topleft[1]+584,topleft[0]+417,topleft[1]+425)).randleft()#bloodalter
    time.sleep(.1)
    Randomize((topleft[0]+1099,topleft[1]+1110,topleft[0]+763,topleft[1]+774)).randleftspeed()#click home tab
    time.sleep(5)

def fill(topleft):
    Randomize((topleft[0]+302,topleft[1]+310,topleft[0]+115,topleft[1]+124)).randleft()#click essenses in bank
    time.sleep(.1)
    Randomize((topleft[0]+1014,topleft[1]+1021,topleft[0]+548,topleft[1]+557)).shiftclick()#pouch1 fill
    time.sleep(.1)
    Randomize((topleft[0]+1057,topleft[1]+1066,topleft[0]+546,topleft[1]+558)).shiftclick()#pouch2 fill
    time.sleep(.1)
    Randomize((topleft[0]+1097,topleft[1]+1108,topleft[0]+546,topleft[1]+561)).shiftclick()#pouch3 fill
    time.sleep(.1)
    Randomize((topleft[0]+1140,topleft[1]+1151,topleft[0]+548,topleft[1]+560)).shiftclick()#pouch4 fill
    time.sleep(.1)
    Randomize((topleft[0]+302,topleft[1]+310,topleft[0]+115,topleft[1]+124)).randleft()#click essenses in bank
    time.sleep(.1)
    Randomize((topleft[0]+1140,topleft[1]+1151,topleft[0]+548,topleft[1]+560)).shiftclick()#pouch4 fill
    time.sleep(.1)
    Randomize((topleft[0]+302,topleft[1]+310,topleft[0]+115,topleft[1]+124)).randleft()#click essenses in bank
    time.sleep(.1)
    Randomize((topleft[0]+701,topleft[1]+708,topleft[0]+43,topleft[1]+52)).randleft()#exit bank
    




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
        pg.moveTo(self.new_x,self.new_y, duration=.08)
        time.sleep(self.random_sleep3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(self.random_sleep3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(self.random_sleep3)
        keyboard.release('shift')

    def move(self):
        pg.moveTo(self.new_x,self.new_y, duration=self.random_sleep2)

    
    def randleftspeed(self):
        pg.moveTo(self.new_x,self.new_y, duration=self.random_sleep3)
        time.sleep(self.random_sleep3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(self.random_sleep3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(self.random_sleep3)
    
    
    def randleft(self):
        pg.moveTo(self.new_x,self.new_y, duration=.3)
        time.sleep(self.random_sleep)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        time.sleep(self.random_sleep)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, self.new_x, self.new_y, 0, 0)
        time.sleep(self.random_sleep)
    
    
    def dragmove(self,x,y):
        pg.moveTo(self.new_x,self.new_y, duration=.3)
        time.sleep(self.random_sleep)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, self.new_x, self.new_y, 0, 0)
        pg.moveTo(x, y, duration=.6)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(self.random_sleep3)
    

class Position():
    def __init__(self, posColor,playerPos=(playerPos)):
        self.pos = posColor
        self.playPos = pg.pixel(playerPos[0],playerPos[1])
    
    def isTrue(self):
        if self.playPos==self.pos:
            return True
        return False

   
class Item():
    def __init__(self, objsRGBVal,screen=(0,0,1920,1080)):
        self.screen = screen
        self.objsRGBVal = objsRGBVal
        self.new_x=0
        self.new_y=0
        
    def findobj(self):
        flag=0
        
        screen=pg.screenshot(region=self.screen)
        time.sleep(.3)
        width, height = screen.size
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                rgb = screen.getpixel((x, y))
                if rgb==self.objsRGBVal:
                    flag = 1
                    new_x= x
                    new_y= y
                    time.sleep(0.05)
                    break
                            
            if flag == 1:
                    return new_x,new_y


class Bag():
    def __init__(self):
        self.lastslot=pg.pixel(1584,982)
        self.first=pg.pixel(1459,766)   
        self.second=pg.pixel(1500,765)
        self.slot25=pg.pixel(1458,983)
        self.slot26=pg.pixel(1500,981)
        self.slot24=Randomize((1578,1585,942,951))
        self.slot28=Randomize((1582,1587,976,984))
        self.cantchisel=False
    def chisel(self):
        if self.first ==white and self.lastslot==yellow:
            return False
        if self.first ==white and self.lastslot==red and self.second == bagcolor:
            return True
    def bloodActive(self):
        if self.slot25 != bloodessActive:
            return True
        return False

    def chiseling(self,num):
        for i in range(num):
            time.sleep(self.slot24.random_sleep3)
            self.slot24.randleftspeed()
            self.slot28.randleftspeed()
            time.sleep(self.slot24.random_sleep3)
    
    
    def isFull(self):
        if self.lastslot == bagcolor:
            return False
        elif self.lastslot == yellow or self.lastslot == red and self.first == white:
            return True
        elif self.lastslot == red and self.first == bagcolor:
            return False
        elif self.first == red and self.lastslot == red:
            return True

         

def makeBox(cord,minMaxX=(0,0),minMaxY=(0,0)):
    
    topleft=(cord[0]+minMaxX[0],cord[0]+minMaxX[1])
    bottomright=(cord[1]+minMaxY[0],cord[1]+minMaxY[1])
    boxcords=(topleft[0],topleft[1],bottomright[0],bottomright[1])
    return boxcords

class Mining():
    def __init__(self):
        try:
            self.climb1pos = Item(climb1)
            self.climb1box=makeBox(self.climb1pos.findobj(),(8,10),(2,4))
        except:
            print('fuck')
        try:
            self.climb2pos = Item(climb2)
            self.climb2box=makeBox(self.climb2pos.findobj(),(2,8),(1,6))
        except:
            print('fuck2')
        
        self.miningcheck=pg.pixel(miningcolor[0],miningcolor[1])

        try:
            self.rock1pos=Item(rock1).findobj()
            self.rock1box=makeBox(self.rock1pos,(25,45),(10,25))

        except:
            print('couldnt find 1')
        try:
            self.rock2pos=Item(rock2).findobj()
            self.rock2box=makeBox(self.rock2pos,(25,30),(10,20))
        except:
            print('couldnt find 2')   
           
    def mining(self):
        if self.miningcheck == red:
            try:
                if pg.pixel(self.rock1pos[0],self.rock1pos[1])==rock1:
                    Randomize(self.rock1box).randleft()
                    time.sleep(5)
            except:
                Randomize(self.rock2box).randleft()
                time.sleep(5)
        else:
            print('mining...')    
    
    def clickclimb1(self):
        Randomize(self.climb1box).randleft()

    def clickclimb2(self):
        Randomize(self.climb2box).randleft()
    
    def mouseclimb1(self):
        Randomize(self.climb1box).move()

    def clickrock1(self):
        Randomize(self.rock1box).randleft()
    
    def mouserock1(self):
        Randomize(self.rock1box).move()
    
    def clickrock2(self):
        Randomize(self.rock2box).randleft()
    
    def mouserock2(self):
        Randomize(self.rock2box).move()

