from stuff import *
import sys
"""zoom set to 200"""
pos1=(255,0,70)
pos2=(255,0,71)
pos3=(255,0,72)
pos4=(255,0,73)
pos5=(255,0,74)
pos6=(255,0,75)
pos7=(255,0,76)
fail1=(0,0,1)
fail2=(0,1,0)
sleep=2

gracecheck=(170,22,13)
nomark=(163,138,98)
laps=0
newtotal=0
total = 0
while True:

    center=pg.pixel(816,530)
    mark = pg.pixel(835,530)
    
    time.sleep(.3)
    
        
    if center == pos1:
        Randomize((807,815,364,371)).randleftspeed()
        time.sleep(sleep)
    elif center == fail1:
        Randomize((921,933,727,739)).randleftspeed()
        time.sleep(sleep)
    elif center == pos2:     
        Randomize((756,764,529,531)).randleftspeed()
        time.sleep(sleep)
    elif center == pos3 and mark == gracecheck:
        Randomize((833,833,528,528)).randleftspeed()
        time.sleep(sleep)
    elif center == pos3 and mark == nomark:
        Randomize((769,777,531,541)).randleftspeed()
        time.sleep(sleep)
    elif center == fail2:
        Randomize((1131,1133,806,807)).randleftspeed()
        time.sleep(sleep)    
    elif center == pos4:
        Randomize((816,822,605,615)).randleftspeed()
        time.sleep(sleep)
    elif center == pos5:
        Randomize((860,866,664,671)).randleftspeed()
        time.sleep(sleep)
    elif center == pos6:
        Randomize((826,834,537,548)).randleftspeed()
        time.sleep(sleep)
        laps+=1
        total = newtotal+laps
        print(f'laps={total}')
        time.sleep(.1)
    
    elif laps == 300 and center == pos7:
        keyboard.press('pageup')
        time.sleep(5)
        keyboard.release('pageup')
        time.sleep(5)
        keyboard.press('f2')
        time.sleep(.5)
        keyboard.release('f2')
        time.sleep(.3)
        print(f'laps={total}')
        time.sleep(sleep)
        newtotal=laps
        laps = 0
    elif center == pos7:
        Randomize((894,902,516,519)).randleftspeed()
        time.sleep(sleep)
        
    
    