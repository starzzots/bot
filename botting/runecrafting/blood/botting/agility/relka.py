import pyautogui as pg
import time
import keyboard
import random
import win32con, win32api
import sys
"""
On startup click compose to face North
set zoom distance to 200
and set so I can look vertical

Remember to look up where I place Checks so I always know where to put them or improve on
"""


running = False
fail1= (961,515)
fail2 = (684,548)

start= (818,409)
check1= (835,594)
check2= (710,684)
check3= (809,575)
check4= (622,563)
check5= (823,452)
final= (655,638)


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
    if checkpixel(1462,767) == (0,0,0):
        sys.exit()
    #failed 1
    elif checkpixel(fail1[0],fail1[1]) == (0,0,0):
        print('Failed spot 1')
        print('Rerouting...')
        left_click_box(836,836,199, 202)
        time.sleep(11)
    
    #failed 2
    elif checkpixel(fail2[0],fail2[1]) == (0,0,0):
        print('Failed spot 2')
        print('Rerouting...')
        left_click_box(694,696,219,220)
        time.sleep(12)
    
    #first click
    elif checkpixel(start[0],start[1]) == (0,0,0):
        print('1 found \ncontinue 1...')
        right_click_box(410,410,518,518)
        time.sleep(13)
        print('passed 1')
    
    #second click first token location chance check
    elif checkpixel(check1[0],check1[1]) == (0,0,0):
        if checkpixel(787,549) == (106,0,0):
            print('Token 1 found \nrouting...')
            left_click_box(783,789,547,553)
            time.sleep(3)
            tokens += 1
            print(f'you have {tokens} tokens')
            left_click_box(793,802,595,621)
            time.sleep(6)
            
        else:
            print('2 found \ncontinue 2...')
            left_click_box(761,784,610,630)
            time.sleep(7)
            print('passed 2')
    
    #third click
    elif checkpixel(check2[0],check2[1]) == (0,0,0):
        print('3 found \ncontinue 3...')
        left_click_box(828,838,679,694)
        time.sleep(10)
        print('passed 3')
    
    #fourth click tokens check 2 and 3
    elif checkpixel(check3[0],check3[1]) == (0,0,0):
        if checkpixel(838,564) == (115,0,0):
            print('Token 2 found routing...')
            left_click_box(836,840,563,569)
            time.sleep(3)
            tokens += 1
            print(f'you have {tokens} tokens')
            print('Countinue from token 2...')
            left_click_box(848,857,456,476)
            time.sleep(12.5)
        elif checkpixel(852,550) == (101,0,0):
            print('Token 3 found routing...')
            left_click_box(848,855,545,551)
            time.sleep(3)
            tokens += 1
            print(f'you have {tokens} tokens')
            print('Countinue from token 3...')
            left_click_box(818,825,472,489)
            time.sleep(12.5)
        else:
            print('4 found. \nContinue 4...')
            left_click_box(850,863,482,501)
            time.sleep(12.5)
            print('passed 4')
    
    #fifth click tokens check 3 and 4
    elif checkpixel(check4[0],check4[1]) == (0,0,0):
        if checkpixel(854,581) == (113,0,0):
            print('Token 4 found \nrouting...')
            left_click_box(852,856,577,582)
            time.sleep(4)
            tokens += 1
            print(f'you have {tokens} tokens')
            left_click_box(847,855,458,476)
            time.sleep(6)
        elif checkpixel(870,567) == (101,0,0):
            print('Token 5 found \nrouting...')
            left_click_box(867,873,560,567)
            time.sleep(4)
            tokens += 1
            print(f'you have {tokens} tokens')
            left_click_box(833,843,472,490)
            time.sleep(5)
        else:
            print('5 found. \nContinue 5...')
            left_click_box(879,891,502,512)
            time.sleep(6.5)
            print('passed 5')
    
    #sixth click
    elif checkpixel(check5[0],check5[1]) == (0,0,0):
        print('6 found. \nContinue 6...')
        left_click_box(880,887,433,443)
        time.sleep(10)
        print('passed 6')
    
    #seventh click
    elif checkpixel(final[0],final[1]) == (0,0,0):
        print('7 found. \nContinue 7...')
        left_click_box(790,812,415,449)
        time.sleep(6)
        print('passed 7')
        laps += 1
        print(f'Laps= {laps}, Tokens= {tokens}')
    else:
        sys.exit()