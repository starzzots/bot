from stuff import *
import sys


green=(0,255,0)
red =(255,0,0)
bagcolor=(62,53,41)

while True:
    slot1=pg.pixel(1456,766)
    lastslot=pg.pixel(1585,978)
    if lastslot == red and slot1 == red:
        Randomize((1450,1464,757,767)).randleftspeed()#click seaweed
        time.sleep(1)
        Randomize((1052,1106,601,678)).randleftspeed()#click fire
        time.sleep(1)
        keyboard.press('space')
        time.sleep(1)
        keyboard.release('space')
        time.sleep(1)

    elif lastslot == red and slot1 == green:
        pass#makking soda just a waiting statement for game

    elif lastslot == green or lastslot == bagcolor:
        Randomize((598,642,364,406)).randleft()#bank
        time.sleep(1)
        Randomize((870,886,817,831)).randleft()#deposit
        time.sleep(1)
        Randomize((565,573,280,286)).randleft()#seaweed
        time.sleep(1)
        Randomize((919,927,62,71)).randleft()#exit


