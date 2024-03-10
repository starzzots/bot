import keyboard
from stuff import *
import sys

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



npc_contact = 0 #npc contact at 8 runs
energy=0 #use ornate pool after 3 runs
sleep=2.5

runs=0
bank = (73,64,52)
bankclick=(255,50,255)
red = (255,0,0)
blood_ruin = (255,77,255)
blood_alter = (0,255,75)
activebloodess=(56,255,255)
yellow=(255,250,0)
wall = (50,87,255)
cave1=(40,8,55)
portal=(14,78,99)

pos1= (0,1,0)
pos2=(0,2,0)
pos3=(0,3,0)
pos4=(0,4,0)
pos5=(0,5,0)
pos6=(0,6,0)
pos7=(0,7,0)
pos8=(0,8,55)

trapdoor = (255,51,255)
passed=0

while True:
    
    if keyboard.is_pressed('q'):
        sys.exit()
    bankcheck=pg.pixel(483,468)
    center=pg.pixel(823,532)
    bagcheck=pg.pixel(1585,983)
    slot1=pg.pixel(1462,765)
    #print(center)
    time.sleep(.1)
    if bankcheck == bank:
        Randomize((662,680,90,109)).randleftspeed()#click ess tab in bank
        time.sleep(.3)
        Randomize((804,816,281,287)).randleftspeed()#essences in bank
        time.sleep(.3)
        Randomize((1535,1545,758,774)).randleftspeed()#small/giant pouch in invo
        time.sleep(.3)
        #Randomize((1575,1585,758,774)).randleftspeed()#medium pouch in invo
        #time.sleep(.1)
        #Randomize((1577,1587,794,808)).randleftspeed()#large pouch in invo
        #time.sleep(.15)
        Randomize((804,816,281,287)).randleftspeed()#essences in bank
        time.sleep(.3)
        Randomize((1535,1545,758,774)).randleftspeed()#small/giant pouch in invo
        time.sleep(.3)
        Randomize((804,816,281,287)).randleftspeed()#essences in bank
        time.sleep(.3)
        Randomize((918,926,59,68)).randleftspeed()#exit bank
        time.sleep(.3)
    elif center == pos1 and bagcheck == red:
        time.sleep(.3)
        trapdoorrect=findobj(trapdoor)
        Randomize((trapdoorrect[0]+10,trapdoorrect[0]+12,trapdoorrect[1]+2,trapdoorrect[1]+3)).randleftspeed()
        time.sleep(sleep)
    elif center == pos2:
        try:
            wallrect=findobj(wall)
            Randomize((wallrect[0]+9,wallrect[0]+9,wallrect[1]+13,wallrect[1]+13)).randleftspeed()
            passed = 1
            time.sleep(7)
            
        except:
            print('oops')    
    elif passed == 1 and center != pos3:
        time.sleep(.3)
        try:
            wallrect=findobj(wall)
            Randomize((wallrect[0]+10,wallrect[0]+10,wallrect[1]+7,wallrect[1]+9)).randleftspeed()
            time.sleep(7)
        except:
            print('oof')
        #Randomize((855,858,626,628)).randleftspeed()#wall click
        #time.sleep(sleep)
    elif center == pos3 and passed == 1:
        time.sleep(.3)
        cave1rect=findobj(cave1)
        Randomize((cave1rect[0]+18,cave1rect[0]+23,cave1rect[1]+15,cave1rect[1]+20)).randleftspeed()
        passed = 0
        time.sleep(sleep)
    elif center == pos4:
        Randomize((866,872,481,486)).randleftspeed()#cave2 click
        time.sleep(sleep)
    elif center ==pos5:
        blood_ruin_rect=findobj(blood_ruin)
        Randomize((blood_ruin_rect[0]+15,blood_ruin_rect[0]+20,blood_ruin_rect[1]+13,blood_ruin_rect[1]+18)).randleftspeed()
        time.sleep(sleep)
    elif center == pos6:
        blood_ruin_alter_rect=findobj(blood_alter)
        Randomize((blood_ruin_alter_rect[0]+18,blood_ruin_alter_rect[0]+25,blood_ruin_alter_rect[1]+13,blood_ruin_alter_rect[1]+18)).randleftspeed()
        time.sleep(sleep)
    elif center == pos7 and slot1 == activebloodess:
        time.sleep(.3)
        Randomize((1535,1545,758,774)).shiftclick()#small pouch in invo
        time.sleep(.2)
        #Randomize((1575,1585,758,774)).shiftclick()#medium pouch in invo
        #time.sleep(.1)
        #Randomize((1577,1587,794,808)).shiftclick()#large pouch in invo
        #time.sleep(.15)
        Randomize((787,801,524,536)).randleftspeed()#blood alter
        time.sleep(.17)
        Randomize((1535,1545,758,774)).shiftclick()#small pouch in invo
        time.sleep(.2)
        #Randomize((1533,1551,793,811)).shiftclick()#giant pouch in invo
        #time.sleep(.11)
        Randomize((787,801,524,536)).randleftspeed()#blood alter
        time.sleep(.17)
        Randomize((1494,1506,973,984)).randleftspeed()#home tab
        #npc_contact+=1
        energy+=1
        time.sleep(4.8)
    elif slot1 != activebloodess:
        time.sleep(.3)
        Randomize((1493,1503,758,766)).randleftspeed()#activate blood boost
        time.sleep(sleep)
    
    
    elif center == pos8 and energy == 2:
        time.sleep(.5)
        Randomize((788,792,485,493)).randleftspeed()#ornate pool
        time.sleep(3)
        portalrect=findobj(portal)
        Randomize((portalrect[0]+12,portalrect[0]+12,portalrect[1]+18,portalrect[1]+18)).randleftspeed()#teleport to kharyll from ornate pool
        time.sleep(4.5)
        energy = 0

    elif center == pos8 and energy != 2:
        portalrect=findobj(portal)
        Randomize((portalrect[0]+15,portalrect[0]+15,portalrect[1]+15,portalrect[1]+15)).randleftspeed()#teleport to kharyll from ornate pool
        time.sleep(7)
    elif center == yellow:
        if runs == 100:
            keyboard.press('pageup')
            time.sleep(5)
            keyboard.release('pageup')
            time.sleep(6.5)
            keyboard.press('x')
            time.sleep(1)
            keyboard.release('x')
            time.sleep(.5)
            runs = 0
            time.sleep(sleep)
        
        else:
            try:
                time.sleep(.3)
                bankclickrect=findobj(bankclick)
                Randomize((bankclickrect[0]+14,bankclickrect[0]+14,bankclickrect[1]+4,bankclickrect[1]+5)).randleftspeed()
                runs+=1
                #print(f'runs={runs}\nnpc_contact={npc_contact}\nenergy={energy}\n')
                print(f'runs={runs}\nenergy={energy}\n')
                time.sleep(6)
            except:
                print('wut')
    else:
        pass
        


#uncomment this if you dont have 99 rcing and need to use npccontact
    """ elif center == pos8 and npc_contact == 9:
        Randomize((1614,1627,715,724)).randleftspeed()#spell book
        time.sleep(.2)
        Randomize((1444,1454,765,771)).randleftspeed()#npc contact
        time.sleep(.2)
        Randomize((673,695,362,395)).randleftspeed()#dark mage
        time.sleep(7)
        keyboard.press('space')
        time.sleep(1)
        keyboard.release('space')
        time.sleep(.3)
        keyboard.press('1')
        time.sleep(1)
        keyboard.release('1')
        time.sleep(.2)
        keyboard.press('space')
        time.sleep(1 )
        keyboard.release('space')
        time.sleep(.3)
        keyboard.press('space')
        time.sleep(1)
        keyboard.release('space')
        time.sleep(.3)
        keyboard.press('space')
        time.sleep(1 )
        keyboard.release('space')
        time.sleep(.3)
        keyboard.press('space')
        time.sleep(1)
        keyboard.release('space')
        time.sleep(.3)
        Randomize((1514,1529,713,726)).randleftspeed()#bag
        time.sleep(.3)
        npc_contact = 0"""