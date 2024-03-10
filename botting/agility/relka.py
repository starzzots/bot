import pyautogui as pg
from stuff import *
"""
On startup click compose to face North
set zoom distance to 200
and set so I can look vertical

Remember to look up where I place Checks so I always know where to put them or improve on
"""

sleep=2

fail1= (0,0,10)
fail2 = (0,0,9)

token1color=(91,10,5)
token2color=(125,111,7)
token3color=(102,10,6)
token4color=(80,8,4)
token5color=(125,111,7)

start= (0,0,2)
check1= (0,0,3)
check2= (0,0,4)
check3= (0,0,5)
check4= (0,0,6)
check5= (0,0,7)
check6= (0,0,8)

token1route=(844,848,541,544)
token2route=(859,862,554,556)
token3route=(847,850,567,568)
token4route=(798,800,541,543)
token5route=(833,835,553,556)

route_from_fail1=(836,837,272,273)
route_from_fail2=(726,728,290,294)

obs1_click=(782,796,594,607)
obs2_click=(831,835,645,651)
obs3_click=(843,859,496,508)
obs4_click=(869,877,507,520)
obs5_click=(866,870,459,465)
obs6_click=(804,818,458,470)
obs7_click=(515,527,520,521)

laps = 150
tokens = 0

while True:
    center=pg.pixel(816,530)
    token1check=pg.pixel(846,543)
    token2check=pg.pixel(858,555)
    token3check=pg.pixel(848,568)
    token4check=pg.pixel(798,545)
    token5check=pg.pixel(833,554)

    if center == start:
        if token4check == token4color:
            Randomize(token4route).randleft()
            time.sleep(3.5)
            Randomize((803,819,580,593)).randleft()
            time.sleep(sleep)
        else:
            Randomize(obs1_click).randleft()
            time.sleep(sleep)
    elif center == check1:
        time.sleep(1)
        Randomize(obs2_click).randleft()
        time.sleep(10)#might need longer sleep timer here if cant find token after rope
    elif center == fail1:
        time.sleep(1)
        Randomize(route_from_fail1).randleft()
        time.sleep(12)
    elif center == check2:
        #add token finding logic in here
        if token1check == token1color:
            Randomize(token1route).randleft()
            time.sleep(2.5)
            Randomize((825,837,488,496)).randleft()
            time.sleep(12)
        elif token5check == token5color:
            Randomize(token5route).randleft()
            time.sleep(3)
            Randomize((841,853,474,484)).randleft()
            time.sleep(12)
        else:
            time.sleep(1)
            Randomize(obs3_click).randleft()
            time.sleep(12)
    elif center == check3:

        #add token finding logic in here
        if token2check == token2color:
            Randomize(token2route).randleft()
            time.sleep(4)
            Randomize((832,838,486,489)).randleft()
            time.sleep(sleep)
        elif token3check == token3color:
            Randomize(token3route).randleft()
            time.sleep(4)
            Randomize((845,848,480,485)).randleft()
            time.sleep(sleep)
        else:
            time.sleep(1)
            Randomize(obs4_click).randleft()
            time.sleep(sleep)
    elif center == fail2:
        time.sleep(1)
        Randomize(route_from_fail2).randleft()
        time.sleep(12)
    elif center == check4:
        time.sleep(1)
        Randomize(obs5_click).randleft()
        time.sleep(sleep)
    elif center == check5:
        time.sleep(1)
        Randomize(obs6_click).randleft()
        time.sleep(6)
    elif center == check6 and laps != 150:
        laps += 1
        print(f'laps= {laps}')
        time.sleep(1)
        Randomize(obs7_click).randleft()
        time.sleep(14)
    elif center == check6 and laps == 150:    
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