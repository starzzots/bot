from stuff import *
import sys

tally = 0
bank = (99,1,237)
bankcheck=(72,62,51)
yellow=(255,255,0)
shop=(255,0,255)
shopcheck=(73,64,52)

bagcolor=(62,53,41)

while True:
    center=pg.pixel(824,525)
    slot1= pg.pixel(1455,768)
    shop_panel=pg.pixel(866,527)
    bank_panel=pg.pixel(904,794)
    
        #Randomize((1514,1526,713,727)).randleft()#bag
        
    if shop_panel == shopcheck:
        Randomize((754,766,444,454)).randleft()#seaweed
        time.sleep(.1)
        Randomize((804,812,445,456)).randleft()#soda
        time.sleep(.3)
        Randomize((916,924,315,323)).randleft()#exit shop
        time.sleep(.2)
        Randomize((1557,1557,145,145)).randleft()
        time.sleep(14)
        bankrect=findobj(bank)
        Randomize((bankrect[0]+15,bankrect[0]+18,bankrect[1]-15,bankrect[1]-12)).randleftspeed()
        time.sleep(15)
    elif bank_panel == bankcheck:
        Randomize((868,888,816,830)).randleft()#deposit
        time.sleep(.2)
        Randomize((914,925,61,70)).randleft()#bank exit
        time.sleep(.2)
        yellowrect=findobj(yellow)
        Randomize((yellowrect[0]+5,yellowrect[0]+10,yellowrect[1]-5,yellowrect[1]-5)).randleftspeed()
        time.sleep(18)
        keyboard.press('pageup')
        time.sleep(5)
        keyboard.release('pageup')
        time.sleep(5)
    else:
        try:
            shoperect=findobj(shop)
            Randomize((shoperect[0]+5,shoperect[0]+6,shoperect[1]+2,shoperect[1]+3)).randleftspeed()
            time.sleep(7)
        except:
            print('wut')