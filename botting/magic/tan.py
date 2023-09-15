from stuff import *
import sys

bdh=(615,625,206,218)
exitbutton=(919,927,62,70)
tan=(1477,1484,858,865)
bankleather=(1453,1463,759,769)
banker=(1206,1255,589,629)
while True:
    if keyboard.is_pressed('q'):
        sys.exit()
    
    Randomize(bdh).randleftspeed()
    time.sleep(.5)
    Randomize(exitbutton).randleftspeed()
    time.sleep(.3)
    for i in range(5):
        Randomize(tan).randleftspeed()
        time.sleep(1.4)
    time.sleep(.3)
    Randomize(banker).randleftspeed()
    time.sleep(.6)
    Randomize(bankleather).randleftspeed()
    time.sleep(.3)


    #19,339,038 starting gp