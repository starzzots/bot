import pyautogui as pg
import time
import keyboard
import random
import win32con, win32api
import sys
"""
zoom 200
"""

running = False
token=(838,529)

check1=(1058,593)
check2=(877,392)
check3=(783,487)
check4=(958,487)
check5=(735,574)
check6=(792,779)
check7=(903,651)

failed = (758,766)
failed2 = (859,493)

random_pix_move_y = random.randrange(25,27,1)
random_pix_move_x = random.randrange(-40,40,8)

random_multi = random.randrange(30,50,1)/100

random_sleep= random.randrange(30,40,1)/100
random_sleep2= random.randrange(10,40,1)/100
random_long_sleep = random.randrange(20,50,1)/100

laps = 0
tokens = 0

def checkpixel(x,y):
    return pg.pixel(x,y)

def right_click_box(x_min, x_max, y_min, y_max):
    new_x = random.randrange(x_min, x_max+1)
    new_y = random.randrange(y_min, y_max+1)
    pg.moveTo(new_x,new_y, duration=random_sleep2)
    time.sleep(random_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,new_x,new_y,0,0)
    time.sleep(random_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,new_x,new_y,0,0)
    time.sleep(random_sleep)
    
    pg.moveTo(new_x + random_pix_move_x, new_y + random_pix_move_y, duration=random_sleep2)
    #win32api.SetCursorPos((new_x + random_pix_move_x, new_y + random_pix_move_y))
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


def quit():
    global running
    running = True
#set hotkey to quit
keyboard.add_hotkey('q',lambda:quit())

while not running:
    if checkpixel(check1[0],check1[1]) == (0,0,0):
        print(f'Tokens= {tokens}  Laps= {laps}')
        print('Course Start Found \nmoving to next location please wait...\n')
        left_click_box(917,932,512,516)
        time.sleep(6)
    elif checkpixel(check2[0],check2[1]) == (0,0,0):
        print('Obstacle 1 found \nmoving to next location please wait...\n')
        left_click_box(806,813,315,325)
        time.sleep(9)
    elif checkpixel(check3[0],check3[1]) == (0,0,0):
        print('Obstacle 2 found \nmoving to next location please wait...\n')
        left_click_box(741,746,526,530)
        time.sleep(8)
    #check for token here too
    elif checkpixel(check4[0],check4[1]) == (0,0,0):
        if checkpixel(token[0],token[1]) == (184,0,0):
            tokens += 1
            print('Token Found \npicking token up please wait...\n')
            left_click_box(835,840,525,532)
            time.sleep(2.3)
            print('Obstacle 3 found \nmoving to next location please wait...\n')
            left_click_box(760,765,530,548)
            time.sleep(3)
        else:
            print('Obstacle 3 found \nmoving to next location please wait...\n')
            left_click_box(760,765,530,548)
            time.sleep(3)

    elif checkpixel(check5[0],check5[1]) == (0,0,0):
        print('Obstacle 4 found \nmoving to next location please wait...\n')
        left_click_box(810,823,629,644)
        time.sleep(4.5)

    elif checkpixel(check6[0],check6[1]) == (0,0,0):
        print('Obstacle 5 found \nmoving to next location please wait...\n')
        left_click_box(872,885,704,714)
        time.sleep(7.7)

    elif checkpixel(check7[0],check7[1]) == (0,0,0):
        print('Obstacle 6 found \nmoving to next location please wait...\n')
        laps += 1
        left_click_box(829,835,540,553)
        time.sleep(12)

    #failed
    elif checkpixel(failed[0],failed[1]) == (0,0,0):
        print('Oops you fell \nmoving to start location please wait...\n')
        left_click_box(953,969,789,802)
        time.sleep(8.7)
    elif checkpixel(failed2[0],failed2[1])==(0,0,0):
        print('Oops you fell spot 2 \nmoving to start location please wait...\n')
        left_click_box(1216,1240,894,910)
        time.sleep(11)
    else:
        print(f'Script end \nTokens= {tokens}, Laps= {laps} \n')
        sys.exit()
