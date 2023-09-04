from pyautogui import *
import pyautogui as pg
import time
import keyboard
import random
import win32con, win32api
from win32gui import FindWindow, GetWindowRect

# FindWindow takes the Window Class name (can be None if unknown), and the window's display text. 
window_handle = FindWindow(None, "RuneLite")
window_rect   = GetWindowRect(window_handle)


random_pix_move_y = random.randrange(25,27,1)
random_pix_move_x = random.randrange(-50,50,2)

random_division = random.randrange(1,30,1)
random_division2 = random.randrange(3,4,1)

random_sleep= random.randrange(1,2,1)/random_division
random_long_sleep = random.randrange(1,3,1)/random_division2


def checkundercharcter():
    x=823
    y=530
    r,g,b = pg.pixel(x,y)
    return r,g,b
def checkpixel(x,y):
    return pg.pixel(x,y)

def right_click_box(x_min, x_max, y_min, y_max):
    new_x = random.randrange(x_min, x_max+1)
    new_y = random.randrange(y_min, y_max+1)
    pg.moveTo(new_x,new_y, duration=random_sleep)
    time.sleep(random_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,new_x,new_y,0,0)
    time.sleep(random_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,new_x,new_y,0,0)
    time.sleep(random_long_sleep)
    
    win32api.SetCursorPos((new_x + random_pix_move_x, new_y + random_pix_move_y))
    time.sleep(random_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, new_x + random_pix_move_x, new_y + random_pix_move_y, 0, 0)
    time.sleep(random_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, new_x + random_pix_move_x, new_y + random_pix_move_y, 0, 0)
    time.sleep(random_sleep)


def left_click_box(x_min, x_max, y_min, y_max):
    new_x = random.randrange(x_min, x_max+1)
    new_y = random.randrange(y_min, y_max+1)
    pg.moveTo(new_x,new_y, duration=.3)
    time.sleep(random_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, new_x, new_y, 0, 0)
    time.sleep(random_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, new_x, new_y, 0, 0)
    time.sleep(random_sleep)



def startcheck():
        
    if checkpixel(787,549) == (106,0,0):
        left_click_box(783,789,547,553)
        time.sleep(3)
        left_click_box(793,802,595,621)
        time.sleep(6)
        #second 
        left_click_box(828,838,680,695)
        time.sleep(11)
          
    else: 
        print('There is no token')
        left_click_box(761,784,610,630)
        time.sleep(7)
        #second 
        left_click_box(828,838,679,694)
        time.sleep(10)
        
def obstacle1():
        #right_click_box(934,841,200,207)
        #time.sleep(11)
        
    
    if checkpixel(838,564) == (115,0,0):
        print('token 1 found')
        left_click_box(836,840,563,569)
        time.sleep(3)
        left_click_box(848,857,456,476)
        time.sleep(13)
        
    if checkpixel(852,550) == (101,0,0):
        print('token 2 found')
        left_click_box(848,855,545,551)
        time.sleep(3)
        left_click_box(818,825,472,489)
        time.sleep(13)
        
    else:
        print('didnt fail obs1')
        left_click_box(850,863,482,501)
        time.sleep(13)
        



def obstacle2():
        
        #right_click_box(691,700,514,519)
        #time.sleep(12)
    if checkpixel(854,581) == (113,0,0):
        print('token found at position 1')
        left_click_box(852,856,577,582)
        time.sleep(4)
        left_click_box(847,855,458,476)
        time.sleep(6)
        #fifth
        left_click_box(877,887,431,444)
        time.sleep(11)
        #finish 
        left_click_box(790,812,415,449)
        time.sleep(8)
    
    if checkpixel(870,565) == (104,0,0):
        print('token found at position 2')
        left_click_box(867,873,560,567)
        time.sleep(4)
        left_click_box(833,843,472,490)
        time.sleep(5)
        #fifth
        left_click_box(880,887,433,443)
        time.sleep(11)
        #finish 
        left_click_box(790,812,415,449)
        time.sleep(8)
        
    else:
        print('passed obs2')
        left_click_box(879,899,502,509)
        time.sleep(8)
        #fifth
        left_click_box(880,887,433,443)
        time.sleep(11)
        #finish 
        left_click_box(790,812,415,449)
        time.sleep(8)
        

def failed_1():
    
    right_click_box(934,841,200,207)
    time.sleep(11)
        

def failed_2():
    
    right_click_box(691,700,514,519)
    time.sleep(12)
    

def restart():

    right_click_box(410,410,518,518)
    time.sleep(13)
        

def fell(a):
    a[0]=False
    a[1]=True
    a[2]=False
    return a

def fell2(a): 
    a[0]=False
    a[1]=False
    a[2]=True
    return a    
    #fullscreen = pg.screenshot(region=(0, 0, 1920, 1080))
    #width, height = fullscreen.size

if checkundercharcter() == (0,0,0):
    print('black')


while True:
    
    states=[True,False,False]
    time.sleep(.5)
    restart()
    time.sleep(.05)
    if states[0] == True:
        startcheck()
        if checkpixel(955,511) == (0,0,0):
            fell(states)
        else:
            obstacle1()
            if checkpixel(687,546) == (0,0,0):
                fell2(states)
            else:
                obstacle2()
    if states[1] == True:
        failed_1()
        startcheck()
        if checkpixel(955,511) == (0,0,0):
            fell(states)
            
        else:
            obstacle1()
            if checkpixel(687,546) == (0,0,0):
                fell2(states)
                
            else:
                obstacle2()
    if states[2] == True:
        failed_2()
        startcheck()

        if checkpixel(955,511) == (0,0,0):
            fell(states)
            
        else:
            obstacle1()
            if checkpixel(687,546) == (0,0,0):
                fell2(states)
                
            else:
                obstacle2()   
        

        
