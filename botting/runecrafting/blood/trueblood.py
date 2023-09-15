import keyboard
import time
from player import *
import pyautogui as pg
import sys
from win32gui import FindWindow, GetWindowRect

"""
set zoom 300
set window runelite to not show name only RuneLite
set RuneLite to 1200,800

"""


'''window_handle = FindWindow(None, 'RuneLite')
window_rect = GetWindowRect(window_handle)
topleft=window_rect[0],window_rect[1]
bottomright=window_rect[0]+760,window_rect[1]+520
new_window_rect = window_rect[0],window_rect[1],window_rect[0]+760,window_rect[1]+500

center=pg.pixel(topleft[0]+390,topleft[1]+282)'''
tally = 0

window_handle = FindWindow(None, 'RuneLite')
window_rect = GetWindowRect(window_handle)
topleft=window_rect[0],window_rect[1]
bottomright=topleft[0]+1200,topleft[1]+800
new_window_rect = topleft[0],topleft[1],bottomright[0],bottomright[1]
#Randomize((topleft[0]+5,topleft[0]+5,topleft[1]+5,topleft[1]+5)).dragmove(2,3)
while True:
    if keyboard.is_pressed('q'):
        sys.exit()
    window_handle = FindWindow(None, 'RuneLite')
    window_rect = GetWindowRect(window_handle)
    topleft=window_rect[0],window_rect[1]
    bottomright=topleft[0]+1200,topleft[1]+800
    new_window_rect = topleft[0],topleft[1],bottomright[0],bottomright[1]
    
    time.sleep(1)
    center=pg.pixel(new_window_rect[0]+604,new_window_rect[1]+431)
    
    pos1=(255,254,0)
    pos2=(255,253,0)
    pos3=(255,252,0)
    pos4=(255,251,0)
    pos5=(255,250,0)
    pos6=(255,249,0)
    pos7=(255,248,0)
    pos8=(255,236,0)
    pos9 = (255,255,0)
    ornatepoolpos=(255,220,0)
    house=(255,241,0)

    
    bank=(255,100,0)
    bankteller=(0,77,255)
    trapdoor=(0,79,255)
    wall=(0,80,255)
    cave_entrance1=(0,81,255)
    cave_entrance2=(0,100,255)
    cave1=(0,71,255)
    cave2=(0,72,255)
    ruin=(0,79,255)
    blood=(0,74,255)
    bonus = (56,255,255)
    activate = (70,255,255)
    ornatepool = (255,0,255)
    portal = (0,76,255)


    """try:
        banktellerbox=Item(bankteller,new_window_rect)
        banktellercords=makeBox(banktellerbox.findobj(),(8,15),(5,7))
        Randomize(banktellercords).randleft()
        time.sleep(1)
    except:
        print('looking for bankteller')"""
    if pg.pixel(topleft[0]+308,topleft[1]+122) == (111,101,101):
        print('we are in the bank')
        if pg.pixel(1099,590)==(62,53,41):
            Randomize((topleft[0]+346,topleft[0]+355,topleft[1]+113,topleft[1]+128)).randleftspeed()
            time.sleep(.2)
        else:
            fill(topleft)
    elif center == bank:
        try:
            trapdoorxy=Item(trapdoor,new_window_rect).findobj()
            trapdoorcords=makeBox(trapdoorxy,(5,5),(-2,0)) #goes to trap door after filling pouches
            Randomize(trapdoorcords).randleft()
            print(tally)
            time.sleep(1)
        except:
            print('cant find trapdoor')
    elif center == pos1:
        try:
            wallxy=Item(wall,new_window_rect).findobj()
            #print(f'wallxy={wallxy}')
            wallcords=makeBox(wallxy,(2,8),(0,0)) #Wall
            #print(f'wallcords={wallcords}')
            Randomize(wallcords).randleft()
            time.sleep(1.5)
        except:
            print('cant find wall')

    elif center == pos2:
        time.sleep(.5)
        Randomize((1101,1103,593,595)).randleft()
        try:
            cave_entrance1xy=Item(cave_entrance1,new_window_rect).findobj()
            cave_entrance1cords=makeBox(cave_entrance1xy,(10,15),(10,15)) #cave_entrance1
            Randomize(cave_entrance1cords).randleft()
            time.sleep(2.2)
        except:
            print('cant find cave_entrance1')

    elif center == pos3:
        time.sleep(.3)
        try:
            cave_entrance2xy=Item(cave_entrance2,new_window_rect).findobj()
            cave_entrance2cords=makeBox(cave_entrance2xy,(0,2),(-1,1)) #cave_entrance2
            Randomize(cave_entrance2cords).randleft()
            time.sleep(.5)
        except:
            print('cant find cave_entrance2')

    elif center == pos4:
        time.sleep(.3)
        try:
            ruinxy=Item(ruin,new_window_rect).findobj()
            ruincords=makeBox(ruinxy,(10,20),(5,30)) #ruin
            Randomize(ruincords).randleft()
            time.sleep(1.5)
        except:
            print('cant find cave1')
    
    elif center == pos7:
        time.sleep(1)
        try:
            bloodxy=Item(blood,new_window_rect).findobj()
            bloodcords=makeBox(bloodxy,(5,15),(-25,-10)) #blood alter
            Randomize(bloodcords).randleft()
            time.sleep(1.5)
        except:
            print('cant find blood alter')
    
    elif center == pos8:
        time.sleep(1)
        if pg.pixel(topleft[0]+1014,topleft[1]+589) == bonus:
            bloodstuff(topleft)
        else:
            Randomize((topleft[0]+1057,topleft[1]+1067,topleft[0]+584,topleft[1]+596)).randleft()#activate blood bonus
    
    elif center == house:
        time.sleep(1)
        tally+=1
        if tally == 7:
            bonusbloods(topleft)
            tally = 0
        else:
            try:
                ornatepoolxy=Item(ornatepool,new_window_rect).findobj()
                ornatepoolcords=makeBox(ornatepoolxy,(0,3),(3,10)) #ornatepool
                Randomize(ornatepoolcords).randleft()
                time.sleep(1.5)
            except:
                print('cant find oranate pool')

    elif center == ornatepoolpos:
        try:
            portalxy=Item(portal,new_window_rect).findobj()
            portalcords=makeBox(portalxy,(2,5),(5,8)) #ornatepool
            Randomize(portalcords).randleft()
            time.sleep(3)
        except:
            print('cant find portal')

    elif center == pos9:
        try:
            banktellerbox=Item(bankteller,new_window_rect)
            banktellercords=makeBox(banktellerbox.findobj(),(5,5),(-3,-3))
            Randomize(banktellercords).randleft()
            time.sleep(5)
        except:
            print('looking for bankteller')