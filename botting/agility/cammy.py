from stuff import *
import sys

pos1=(0,0,1)
pos2=(0,1,2)
pos3=(0,0,3)
pos4=(0,0,4)
pos5=(0,0,5)
pos6=(0,0,6)
fail=(0,0,32)
obs1=(713,723,483,505)
obs2=(784,792,585,591)
obs3=(821,839,573,579)
obs4=(707,723,562,569)
obs5=(831,837,548,557)
obs6=(1114,1115,233,233)
tok1=(798,802,505,509)
tok2=(740,742,539,542)
tok3=(844,848,518,520)
tok4= (775,779,528,533)
tok5=(774,776,541,544)
colort=(205,0,0)
ct1=(205,175,15)
ct3=(205,174,15)
ct5=(205,185,16)
sleep=2
laps=0

while True:
    center=pg.pixel(816,530)
    token1= pg.pixel(795,507)
    token2=pg.pixel(736,539)
    token3=pg.pixel(845,520)
    token4= pg.pixel(771,526)
    token5= pg.pixel(777,543)
    if center == pos1:
        time.sleep(sleep)
        if token1 == colort or pg.pixel(799,508)== ct1:
            time.sleep(sleep)
            Randomize(tok1).randleft()
            time.sleep(sleep)
            Randomize((736,742,505,521)).randleft()
            time.sleep(5)
        else:
            time.sleep(sleep)
            Randomize(obs1).randleft()
            time.sleep(sleep)
    elif center == pos2:
        time.sleep(sleep)
        if token2 == colort:
            time.sleep(2)
            Randomize(tok2).randleft()
            time.sleep(4)
            Randomize((865,871,575,581)).randleft()
            time.sleep(8)
        elif token5 == ct5:
            time.sleep(sleep)
            Randomize(tok5).randleft()
            time.sleep(4)
            Randomize((832,836,575,580)).randleft()
            time.sleep(2)
        else:
            time.sleep(sleep)
            Randomize(obs2).randleft()
            time.sleep(sleep)
    elif center == fail:
        time.sleep(sleep)
        Randomize((1046,1046,473,473)).randleft()
        time.sleep(sleep)
    elif center == pos3:
        time.sleep(sleep)
        if token3 == ct3 or pg.pixel(846,521) == ct3:
            time.sleep(2)
            Randomize(tok3).randleft()
            time.sleep(4)
            Randomize((806,824,587,592)).randleft()
            time.sleep(2)
        else:
            time.sleep(sleep)
            Randomize(obs3).randleft()
            time.sleep(sleep)
    
    elif center == pos4:
        time.sleep(sleep)
        Randomize(obs4).randleft()
        time.sleep(sleep)
    elif center == pos5:
        time.sleep(sleep)
        if token4 == colort:
            time.sleep(2)
            Randomize(tok4).randleft()
            time.sleep(3.4)
            Randomize((876,882,549,559)).randleft()
            time.sleep(8)
        else:
            time.sleep(2)
            Randomize(obs5).randleft()
            time.sleep(4)
    elif center == pos6 and laps != 150:
        time.sleep(sleep)
        Randomize(obs6).randleft()
        time.sleep(4)
        laps += 1
        print(laps)
        
    elif center == pos6 and laps == 150:    
        keyboard.press('page down')
        time.sleep(.2)
        keyboard.release('page down')
        
        time.sleep(10)
        keyboard.press('x')
        time.sleep(.2)
        keyboard.release('x')
        time.sleep(.2)
        laps = 0
        print(laps)
        time.sleep(3)
    else:
        pass
