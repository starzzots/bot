import keyboard
from stuff import *
import sys
import win32gui

"""
set zoom 300
set window runelite to not show name only RuneLite
set RuneLite to 700,600 lock screen
turn runelite title player name off

"""


'''window_handle = FindWindow(None, 'RuneLite')
window_rect = GetWindowRect(window_handle)
topleft=window_rect[0],window_rect[1]
bottomright=window_rect[0]+760,window_rect[1]+520
new_window_rect = window_rect[0],window_rect[1],window_rect[0]+760,window_rect[1]+500

center=pg.pixel(topleft[0]+390,topleft[1]+282)'''


hwnd = win32gui.FindWindow(None, 'RuneLite')
window_rect = win32gui.GetWindowRect(hwnd)

#pg.moveTo(window_rect[0]+2,window_rect[1]+2)

Randomize((window_rect[0]+5,window_rect[0]+5,window_rect[1]+5,window_rect[1]+5)).dragmove(7,7)

npc_contact = 0 #npc contact at 8 runs
energy=2  #use ornate pool after 3 runs
sleep=2.5

runs=0

bank = (70,61,50)
bankclick=(255,50,255)
red = (255,0,0)
blood_ruin = (255,77,255)
blood_alter = (0,255,75)
activebloodess=(56,255,255)
yellow=(255,250,0)
wall = (50,87,255)
cave1=(40,8,55)
portal=(14,78,99)
ess_pos_bank= (372,382,263,271)
giant_pouch = (662,677,352,361)
floor=(50,50,189)

pos1= (0,1,0)
pos2=(0,2,0)
pos3=(0,3,0)
pos4=(0,4,0)
pos5=(0,5,0)
pos6=(0,6,0)
pos7=(0,7,0)
pos8=(0,8,55)

trapdoor = (255,51,255)


while True:
    if keyboard.is_pressed('q'):
        sys.exit()
    bankcheck=pg.pixel(442,86)
    center=pg.pixel(384,330)
    bagcheck = pg.pixel(714,359)
    slot1=pg.pixel(584,359)

    
    time.sleep(.1)
    if bankcheck == bank:
        Randomize((234,249,76,91)).randleftspeed()#click ess tab in bank
        time.sleep(.3)
        Randomize(ess_pos_bank).randleftspeed()#essences in bank
        time.sleep(.3)
        Randomize(giant_pouch).randleftspeed()#small/giant pouch in invo
        time.sleep(.3)
        #Randomize((1575,1585,758,774)).randleftspeed()#medium pouch in invo
        #time.sleep(.1)
        #Randomize((1577,1587,794,808)).randleftspeed()#large pouch in invo
        #time.sleep(.15)
        Randomize(ess_pos_bank).randleftspeed()#essences in bank
        time.sleep(.3)
        Randomize(giant_pouch).randleftspeed()#small/giant pouch in invo
        time.sleep(.3)
        Randomize(ess_pos_bank).randleftspeed()#essences in bank
        time.sleep(.3)
        Randomize((485,490,44,51)).randleftspeed()#exit bank
        time.sleep(.3)
    elif center == pos1 and bagcheck == red:
        time.sleep(.3)
        trapdoorrect=findobj(trapdoor)
        Randomize((trapdoorrect[0]+3,trapdoorrect[0]+7,trapdoorrect[1]+5,trapdoorrect[1]+5)).randleftspeed()
        time.sleep(sleep)
    elif center == pos2:
        try:
            wallrect=findobj(wall)
            Randomize((wallrect[0]+5,wallrect[0]+5,wallrect[1]+11,wallrect[1]+12)).randleftspeed()
            time.sleep(sleep)
        except:
            print('oops')
        #Randomize((855,858,626,628)).randleftspeed()#wall click
        #time.sleep(sleep)
    elif center == pos3:
        time.sleep(.3)
        floorrect=findobj(floor)
        Randomize((floorrect[0]+7,floorrect[0]+10,floorrect[1]+8,floorrect[1]+10)).randleftspeed()
        time.sleep(sleep)
    elif center == floor:
        cave1rect=findobj(cave1)
        Randomize((cave1rect[0]+3,cave1rect[0]+5,cave1rect[1]+5,cave1rect[1]+10)).randleftspeed()
        time.sleep(sleep)
    elif center == pos4:
        Randomize((415,416,300,302)).randleftspeed()#cave2 click
        time.sleep(sleep)
    elif center ==pos5:
        blood_ruin_rect=findobj(blood_ruin)
        Randomize((blood_ruin_rect[0]+10,blood_ruin_rect[0]+15,blood_ruin_rect[1]+13,blood_ruin_rect[1]+15)).randleftspeed()
        time.sleep(sleep)
    elif center == pos6:
        blood_ruin_alter_rect=findobj(blood_alter)
        Randomize((blood_ruin_alter_rect[0]+8,blood_ruin_alter_rect[0]+16,blood_ruin_alter_rect[1]+5,blood_ruin_alter_rect[1]+8)).randleftspeed()
        time.sleep(sleep)
    elif center == pos7 and slot1 == activebloodess:
        time.sleep(.3)
        Randomize(giant_pouch).shiftclick()#small pouch in invo
        time.sleep(.2)
        #Randomize((1575,1585,758,774)).shiftclick()#medium pouch in invo
        #time.sleep(.1)
        #Randomize((1577,1587,794,808)).shiftclick()#large pouch in invo
        #time.sleep(.15)
        Randomize((365,370,327,330)).randleftspeed()#blood alter
        time.sleep(.17)
        Randomize(giant_pouch).shiftclick()#small pouch in invo
        time.sleep(.2)
        #Randomize((1533,1551,793,811)).shiftclick()#giant pouch in invo
        #time.sleep(.11)
        Randomize((365,370,327,330)).randleftspeed()#blood alter
        time.sleep(.17)
        Randomize((624,632,567,575)).randleftspeed()#home tab
        #npc_contact+=1
        energy+=1
        time.sleep(4.8)
    elif slot1 != activebloodess:
        time.sleep(.3)
        Randomize((625,629,351,357)).randleftspeed()#activate blood boost
        time.sleep(sleep)
    
    
    elif center == pos8 and energy == 2:
        time.sleep(.5)
        Randomize((368,369,299,300)).randleftspeed()#ornate pool
        time.sleep(3)
        portalrect=findobj(portal)
        Randomize((portalrect[0]+8,portalrect[0]+9,portalrect[1]+10,portalrect[1]+13)).randleftspeed()#teleport to kharyll from ornate pool
        time.sleep(sleep)
        energy = 0

    elif center == pos8 and (npc_contact != 9 or energy != 2):
        portalrect=findobj(portal)
        Randomize((portalrect[0]+8,portalrect[0]+9,portalrect[1]+10,portalrect[1]+13)).randleftspeed()#teleport to kharyll from ornate pool
        time.sleep(sleep)
    elif center == yellow:
        if runs == 175:
            keyboard.press('pageup')
            time.sleep(5)
            keyboard.release('pageup')
            time.sleep(6.5)
            keyboard.press('f2')
            time.sleep(1)
            keyboard.release('f2')
            time.sleep(.5)
            runs=0
            time.sleep(sleep)
        try:
            time.sleep(.3)
            bankclickrect=findobj(bankclick)
            Randomize((bankclickrect[0]+11,bankclickrect[0]+12,bankclickrect[1]+2,bankclickrect[1]+5)).randleftspeed()
            runs+=1
            #print(f'runs={runs}\nnpc_contact={npc_contact}\nenergy={energy}\n')
            print(f'runs={runs}\nenergy={energy}\n')
            time.sleep(6)
        except:
            print('wut')
    else:
        pass