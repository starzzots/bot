from stuff import *
import sys

lightblue=(70,255,255)
white=(255,255,255)
green=(0,255,0)
red =(255,0,0)
yellow=(255,255,0)
bagcolor=(62,53,41)
sandpit=(255,0,255)
bankchest=(255,71,0)
tally=0

while True:
    center=pg.pixel(820,531)
    slot1=pg.pixel(1456,766)
    slot2=pg.pixel(1498,764)
    lastslot=pg.pixel(1546,979)
    bank=pg.pixel(840,735)
    if keyboard.is_pressed('q'):
        sys.exit()
    
    elif bank == (73,64,52):
        if slot1 == bagcolor:
            Randomize((614,624,280,286)).randleft()#duel ring
        elif slot2 == bagcolor and slot1 == white:
            Randomize((518,528,281,289)).randleft()#empty buckets
            time.sleep(.3)
            Randomize((916,925,61,70)).randleft()#exit bank
            time.sleep(.3)
        elif slot2 == green:
            Randomize((1494,1504,759,771)).randleft()
            time.sleep(.3)
    
    else:
        if slot1 == white and slot2 == red:
            Randomize((1614,1627,715,724)).randleft()#spell book
            time.sleep(.2)
            Randomize((1445,1460,889,900)).randleft()#house teleport
            time.sleep(.3)
            Randomize((1514,1529,713,726)).randleft()#bag
            time.sleep(.3)
            Randomize((1494,1501,762,767)).randleft()#empty bucket
            time.sleep(.4) 
            sandpitrect=findobj(sandpit)
            Randomize((sandpitrect[0]+15,sandpitrect[0]+25,sandpitrect[1]+8,sandpitrect[1]+15)).randleft()#sandpit
            time.sleep(5)
        elif slot2 == green and lastslot == red:
            pass
        elif lastslot == green:
    
            Randomize((1454,1462,765,774)).randleft()#duel ring
            time.sleep(.3)
            Randomize((217,302,942,946)).randleft()#castle wars option
            time.sleep(3)
            bankrect=findobj(bankchest)
            Randomize((bankrect[0]+5,bankrect[0]+15,bankrect[1]+8,bankrect[1]+15)).randleft()#bank click
            time.sleep(4)
            tally +=1
            print(f'total buckets made = {tally*26}')
        
        