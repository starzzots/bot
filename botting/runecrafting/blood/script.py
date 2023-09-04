import keyboard
import time
from player import *
import pyautogui as pg
import sys
running = False

   
def quit():
    global running
    running = True

keyboard.add_hotkey('q',lambda:quit())

class Runescrafting():
    def __init__(self):
        self.pos1 = Position(pos1Color)
        self.pos2 = Position(pos2Color)
        self.pos3 = Position(pos3Color)
        self.pos4 = Position(pos4Color)
        self.pos5 = Position(pos5Color)
        self.pos6 = Position(pos6Color)
        self.pos7 = Position(pos7Color)
        self.pos8 = Position(pos8Color)
        self.pos9 = Position(yellow)
        self.darkalterpos = Item(darkalter)
        self.bloodalterpos = Item(bloodalter)
        #print(f'\nleftcolor:{playerPosL} rightcolor:{playerPosR} upcolor:{playerPosU} downcolor:{playerPosD}')
        #print(f'PlayerColor:{playerPosColor}\n')
        
    
    #need to figure out how to make states should only need 2. all start at first starts at pos1 and second has to come back into POS1
    # one for mining and going to alter and back mining 
    #and on that cant go from mining darkalter to blood alter then back to pos1
    
    def blood(self):
        miningcheck = pg.pixel(miningcolor[0],miningcolor[1])
        playerU=pg.pixel(playerPos[0],playerPos[1]-8)
        playerD=pg.pixel(playerPos[0],playerPos[1]+8)
        try:
            self.darkalterrect=makeBox(self.darkalterpos.findobj(),(30,80),(0,20))
            self.darkalteropts=Randomize(self.darkalterrect)
            self.bloodalterrect=makeBox(self.bloodalterpos.findobj(),(20,45),(0,60))
            self.bloodalteropts=Randomize(self.bloodalterrect)
        except:
            pass  
        if Bag().slot25 == bloodessActive:
            if Bag().isFull()==False:
                if self.pos1.isTrue() or (self.pos2.isTrue() or self.pos3.isTrue())or (playerU == pos3Color or playerD ==pos2Color):
                    Mining().mining()
                elif self.pos5.isTrue() and Bag().first == white and Bag().lastslot == bagcolor and playerU == pos5Color:
                    try:
                        Mining().clickclimb1()
                        time.sleep(1)
                    except:
                        pass
                elif self.pos4.isTrue() and Bag().first == white and Bag().lastslot == bagcolor:
                    time.sleep(2)
                    self.climb1pos=Item(climb1).findobj()
                    self.climb1box=makeBox(self.climb1pos,(2,10),(3,8))
                    Randomize(self.climb1box).randleft()
                    time.sleep(3)

                elif self.pos8.isTrue() and playerD==pos8Color:
                    try:
                        self.rock1pos=Item(rock1).findobj()
                        self.rock1box=makeBox(self.rock1pos,(25,65),(25,55))
                        if pg.pixel(self.rock1pos[0],self.rock1pos[1])==rock1:
                            Randomize(self.rock1box).randleft()
                            time.sleep(15)
                    except:
                        print('gayyy')
                elif self.pos1.isTrue() and miningcheck == red:
                    Mining().mining()

                elif self.pos7.isTrue() and Bag().first == white:
                    try:
                        Randomize((767,790,483,500)).randleft()
                        time.sleep(1)
                        Randomize((1790,1799,200,255)).move()
                        
                    except:
                        print('wut')
                    time.sleep(2)
                elif self.pos7.isTrue() and Bag().lastslot == red and Bag().first == bagcolor:
                    time.sleep(1)
                    Bag().chiseling(24)
                elif self.pos7.isTrue() and Bag().first == bagcolor and Bag().lastslot == bagcolor:
                    Randomize((1790,1799,200,255)).move()
                    try:
                        self.climb2pos = Item(yellow)
                        self.climb2box=makeBox(self.climb2pos.findobj(),(13,18),(70,70))
                        Randomize(self.climb2box).randleft()
                        time.sleep(15)
                    except:
                        print('ugh')
                elif self.pos9.isTrue() and Bag().first == bagcolor and Bag().lastslot == bagcolor:
                    try:
                        self.climb2pos = Item(yellow)
                        self.climb2box=makeBox(self.climb2pos.findobj(),(15,18),(13,18))
                        Randomize(self.climb2box).randleft()
                        time.sleep(3)
                    except:
                        print('ugh')
                

                else:
                    print('1')
                    print(self.pos7.isTrue())
                    print(pg.pixel(playerPos[0],playerPos[1]))

            
            elif Bag().isFull()==True:
                if self.pos2.isTrue() or self.pos3.isTrue():
                    try:
                        Mining().clickclimb1()
                        time.sleep(8)
                    except:
                        print('I eat ass')
                elif self.pos4.isTrue():
                    time.sleep(1)
                    self.darkalteropts.randleft()
                    time.sleep(5)
                elif self.pos5.isTrue() and Bag().lastslot ==red and Bag().first == red:
                    Bag().chiseling(24)
                    time.sleep(1)
                elif self.pos5.isTrue() and Bag().lastslot ==red and Bag().second==red:
                    time.sleep(1)
                    Randomize((1586,1588,163,165)).randleft()
                    time.sleep(1)
                elif self.pos6.isTrue():
                    try:
                        time.sleep(2)
                        self.bloodalterpos = Item(bloodalter)
                        self.bloodalterbox=makeBox(self.bloodalterpos.findobj(),(20,27),(10,30))
                        Randomize(self.bloodalterbox).randleft()
                        time.sleep(5)
                    except:
                        pass
                elif self.pos2.isTrue() or self.pos3.isTrue():
                    try:
                        Mining().clickclimb1()
                    except:
                        print('asdfae fuck fuck fuck')
                else:
                    print('looking for task...')
                    print(self.pos5.isTrue())
                    print(pg.pixel(playerPos[0],playerPos[1]))
        
        
        #no bloodess
        else:
            Randomize((1495,1505,974,989)).randleft()
            time.sleep(1)
            Randomize((1451,1463,759,771)).dragmove(1452,980)
            time.sleep(1)
            



     
while True:
    if keyboard.is_pressed('q'):
        sys.exit()
    
    
    Runescrafting().blood()
    
            