from stuff import *
import pyautogui
# 25 zooom

#locations
dwarf=(819,826,501,509)
store=(519,526,303,310)
bankexitbutton=(920,928,60,71)
coalbag=(1498,1509,762,768)
dump=(1497,1512,757,770)
exitbutton=(919,928,316,322)
coal = (805,814,350,360)
bank=(1112,1124,748,761)

slot3=(1540,1552,763,768)
count=0
sleep = 1.1
while True:
    if count < 2:
        Randomize(store).randleft()
        time.sleep(5)
        Randomize(coal).randleft()
        time.sleep(sleep)
        Randomize(exitbutton).randleft()
        time.sleep(sleep)
        Randomize(coalbag).randleft()
        time.sleep(sleep)
        Randomize(dwarf).randleft()
        time.sleep(sleep)
        Randomize(coal).randleft()
        time.sleep(sleep)
        Randomize(bank).randleft()
        time.sleep(5)
        Randomize(coalbag).randleft()
        time.sleep(sleep)
        Randomize(slot3).randleft()
        time.sleep(sleep)
        Randomize(bankexitbutton).randleft()
        time.sleep(sleep)
        count += 1
    else:
        keyboard.press('pageup')
        time.sleep(.5)
        keyboard.release('pageup')
        time.sleep(10)
        keyboard.press('x')
        time.sleep(.2)
        keyboard.release('x')
        time.sleep(.2)
        count = 0
    
#Randomize(fillcoal).move()
#pyautogui.moveTo(coal)
#print(dwarfLoc)
#pyautogui.moveTo(dwarfLoc)