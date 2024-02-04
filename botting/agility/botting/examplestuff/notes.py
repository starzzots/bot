"""
                elif playerPosU == pos6:
                    print('pos 6 found click dark alter')
                    Mouse((darkalterrect[0]+10,darkalterrect[1]+10),(darkalterrect[0]+30,darkalterrect[1]+30)).leftrand()
                    time.sleep(.5)
                    time.sleep(.5)
                    
                elif playerPosR == pos7:
                    print('pos 7 bag not full going back to mine')
                    Mouse((climb1rect[0]+5,climb1rect[1]),(climb1rect[0]+13,climb1rect[1])).leftrand()
                    time.sleep(.5)
                
                elif playerPosR==pos10:
                    print('find climb 2 and switch cantchiesel to False')
                    cantchisel = False
                    Mouse((climb2rect[0]+5,climb2rect[1]+36),(climb2rect[0]+13,climb2rect[1]+38)).leftrand()
                    time.sleep(4)

                else:
                    print(f'looking for task mining pitstuff reeeeeee... c={cantchisel},b={bagfull}')
                   
    

            elif first == white and lastslot != yellow:
                #need plug in dark alter logic here
                cantchisel == True
                if playerPosD == pos2:
                    print("Pos2 (50,255,0)\n")
                    
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                #pos3
                elif playerPosU == pos3:
                    print("Pos3 (51,255,0)\n")
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                #pos4
                elif playerPosL == pos4:
                    print("Pos4 (52,255,0)\n")
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                #pos5
                elif playerPosD == pos5:
                    print("Pos5 (53,255,0)\n")
                    time.sleep(.5)
                #pos6
                elif playerPosU == pos6:
                    print("Pos6 need to go back to darkalter (54,255,0)\n")
                    Mouse((darkalterrect[0]+10,darkalterrect[1]+10),(darkalterrect[0]+30,darkalterrect[1]+30)).leftrand()
                    time.sleep(1)
                            
                
                else:
                    print(f'cant find what to do reeeee... c={cantchisel}, b={bagfull}')     
            
            elif first == white and second == red:
                if playerPosR == pos7:
                    print('heading to blood alter...')
                    Mouse((1588,171),(1590,172)).leftrand()
                    time.sleep(2)
                elif playerPosD == pos9:
                    print('Youve made it to pos9 click on blood alter...')
                    Mouse((bloodalterrect[0]+20,bloodalterrect[1]+30),(bloodalterrect[0]+40,bloodalterrect[1]+50)).leftrand()
                    time.sleep(2)
            elif first == bagcolor and lastslot == red:
                if playerPosR == pos10:
                    cantchisel=False
                    print(f'chiseling... c={cantchisel},b={bagfull}')
            elif first == white and lastslot == red:
                print(f'looking for task 7 chisel... c={cantchisel},b={bagfull}')
                time.sleep(.5)
                if playerPosD == pos2:
                    print("Pos2 (50,255,0)\n")
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                #pos3
                elif playerPosU == pos3:
                    print("Pos3 (51,255,0)\n")
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                #pos4
                elif playerPosL == pos4:
                    print("Pos4 (52,255,0)\n")
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                elif playerPosU == pos6:
                    print("Pos6 (54,255,0)\n")
                    Mouse((darkalterrect[0]+10,darkalterrect[1]+10),(darkalterrect[0]+30,darkalterrect[1]+30)).leftrand()
                    time.sleep(.5)
                
                else:
                    if playerPosR == pos7:
                        print('start chiseling....1234')
                        chiseling()
                        cantchisel= True
                    print(f'cant find what to do reeeee... c={cantchisel}, b={bagfull}')
        #bag full
        else:
            if first == yellow:

                if playerPosD == pos2:
                    print("Pos2 (50,255,0)\n")
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                #pos3
                elif playerPosU == pos3:
                    print("Pos3 (51,255,0)\n")
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                #pos4
                elif playerPosL == pos4:
                    print("Pos4 (52,255,0)\n")
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                elif playerPosU == pos6:  
                    cantchisel = True
                    print('pos 6 found click on climb1 should be next to it')
                    Mouse((climb1rect[0]+8,climb1rect[1]+8),(climb1rect[0]+13,climb1rect[1]+10)).leftrand()
                    time.sleep(.5)
                
            elif lastslot == red:
                if playerPosR == pos7:
                    print('chiseling...')
                    chiseling()
                elif playerPosL == pos9:
                    print('click on blood alter from pos9')
                    Mouse((bloodalterrect[0]+20,bloodalterrect[1]+30),(bloodalterrect[0]+40,bloodalterrect[1]+50)).leftrand()
                    time.sleep(3) 
            
                
            else:
                print(f'c={cantchisel},b={bagfull}')
    
   
    else:#cant chisel = True
        
        if bagfull == False:
            if lastslot != red:
                bagfull = False
                if playerPosColor == pos1:
                    print('Pos1 False(0,0,0)\n')
                    try:
                        rock1check=checkpixel(rock1rect[0],rock1rect[1])
                        if miningcolor == red and rock1check == rock1:
                            print('Not Mining')
                            mining=False
                            Mouse((rock1rect[0]+20,rock1rect[1]+20),(rock1rect[0]+30,rock1rect[1]+55)).leftrand()
                            time.sleep(.5)
                        elif lastslot == yellow:
                            bagfull = True
                        elif first == white and lastslot == yellow:
                            bagfull = True
                    except:
                        rock2check=checkpixel(rock2rect[0],rock2rect[1])
                        if miningcolor == red and rock2check==rock2:
                            print('Not Mining')
                            mining=False
                            Mouse((rock2rect[0]+20,rock2rect[1]+20),(rock2rect[0]+30,rock2rect[1]+50)).leftrand()
                            time.sleep(.5)
                        elif lastslot == yellow:
                            bagfull = True
                        elif first == white and lastslot == yellow:
                            bagfull = True

            
                #position 2 logic 
                elif playerPosD == pos2:
                    print('Pos2 not full cant chisel True(50,255,0)\n')
                    
                    if miningcolor == green:
                        print('mining rock1...')
                    elif miningcolor == red:
                        try:
                            rock1check=checkpixel(rock1rect[0],rock1rect[1])
                            if miningcolor == red and rock1check == rock1:
                                print('Not Mining')
                                mining=False
                                Mouse((rock1rect[0]+20,rock1rect[1]+20),(rock1rect[0]+40,rock1rect[1]+55)).leftrand()
                                time.sleep(.5)
                            elif lastslot == yellow:
                                bagfull = True
                            elif first == white and lastslot == yellow:
                                bagfull = True


                        except:
                            rock2check=checkpixel(rock2rect[0],rock2rect[1])
                            if miningcolor == red and rock2check==rock2:
                                print('Not Mining')
                                mining=False
                                Mouse((rock2rect[0]+20,rock2rect[1]+20),(rock2rect[0]+30,rock2rect[1]+50)).leftrand()
                                time.sleep(.5)
                            elif lastslot == yellow:
                                bagfull = True
                            elif first == white and lastslot == yellow:
                                bagfull = True
                    #position 3 logic 
                elif playerPosD == pos3:
                    print('Pos2 (51,255,0)\n')
                    
                    if miningcolor == green:
                        print('mining rock2...')
                    elif miningcolor == red:
                        try:
                            rock1check=checkpixel(rock1rect[0],rock1rect[1])
                            if miningcolor == red and rock1check == rock1:
                                print('Not Mining')
                                mining=False
                                Mouse((rock1rect[0]+20,rock1rect[1]+20),(rock1rect[0]+40,rock1rect[1]+55)).leftrand()
                                time.sleep(.5)
                            elif lastslot == yellow:
                                bagfull = True
                            elif first == white and lastslot == yellow:
                                bagfull = True


                        except:
                            rock2check=checkpixel(rock2rect[0],rock2rect[1])
                            if miningcolor == red and rock2check==rock2:
                                print('Not Mining')
                                mining=False
                                Mouse((rock2rect[0]+20,rock2rect[1]+20),(rock2rect[0]+30,rock2rect[1]+50)).leftrand()
                                time.sleep(.5)
                            elif lastslot == yellow:
                                bagfull = True
                            elif first == white and lastslot == yellow:
                                bagfull = True
                    

                #pos 4
                elif playerPosL == pos4:
                    if miningcolor == green:
                        print('mining rock2...')
                    elif miningcolor == red:
                        try:
                            rock1check=checkpixel(rock1rect[0],rock1rect[1])
                            if miningcolor == red and rock1check == rock1:
                                print('Not Mining')
                                mining=False
                                Mouse((rock1rect[0]+20,rock1rect[1]+20),(rock1rect[0]+40,rock1rect[1]+55)).leftrand()
                                time.sleep(.5)
                            elif lastslot == yellow:
                                bagfull = True
                            elif first == white and lastslot == yellow:
                                bagfull = True
                            

                        except:
                            rock2check=checkpixel(rock2rect[0],rock2rect[1])
                            if miningcolor == red and rock2check==rock2:
                                print('Not Mining')
                                mining=False
                                Mouse((rock2rect[0]+20,rock2rect[1]+20),(rock2rect[0]+30,rock2rect[1]+50)).leftrand()
                                time.sleep(.5)
                            elif lastslot == yellow:
                                bagfull = True
                            elif first == white and lastslot == yellow:
                                bagfull = True
                                
                #pos5
                elif playerPosD == pos5:
                    
                    if miningcolor == green:
                        print('mining rock1...')
                    elif first == white and lastslot == bagcolor:
                        try:
                            rock1check=checkpixel(rock1rect[0],rock1rect[1])
                            if miningcolor == red and rock1check == rock1:
                                print('Not Mining')
                                mining=False
                                Mouse((rock1rect[0]+20,rock1rect[1]+20),(rock1rect[0]+40,rock1rect[1]+55)).leftrand()
                                time.sleep(.5)
                            elif lastslot == yellow:
                                bagfull = True
                            elif first == white and lastslot == yellow:
                                bagfull = True

                        except:
                            rock2check=checkpixel(rock2rect[0],rock2rect[1])
                            if miningcolor == red and rock2check==rock2:
                                print('Not Mining')
                                mining=False
                                Mouse((rock2rect[0]+20,rock2rect[1]+20),(rock2rect[0]+30,rock2rect[1]+50)).leftrand()
                                time.sleep(.5)
                            elif lastslot == yellow:
                                bagfull = True
                            elif first == white and lastslot == yellow:
                                bagfull = True
                    elif miningcolor == red:
                        try:
                            rock1check=checkpixel(rock1rect[0],rock1rect[1])
                            if miningcolor == red and rock1check == rock1:
                                print('Not Mining')
                                mining=False
                                Mouse((rock1rect[0]+20,rock1rect[1]+20),(rock1rect[0]+40,rock1rect[1]+55)).leftrand()
                                time.sleep(.5)
                            elif lastslot == yellow:
                                bagfull = True
                            elif first == white and lastslot == yellow:
                                bagfull = True

                        except:
                            rock2check=checkpixel(rock2rect[0],rock2rect[1])
                            if miningcolor == red and rock2check==rock2:
                                print('Not Mining')
                                mining=False
                                Mouse((rock2rect[0]+20,rock2rect[1]+20),(rock2rect[0]+30,rock2rect[1]+50)).leftrand()
                                time.sleep(.5)
                            elif lastslot == yellow:
                                bagfull = True
                            elif first == white and lastslot == yellow:
                                bagfull = True
                elif playerPosR == pos7:
                    print(f'head to blood alter pos9...c={cantchisel},b={bagfull}')
                    Mouse((1588,171),(1590,172)).leftrand()
                    time.sleep(2)
                elif playerPosL == pos9:
                    print(f'click on blood alter from pos 9... c={cantchisel}, b={bagfull}')
                    Mouse((bloodalterrect[0]+20,bloodalterrect[1]+30),(bloodalterrect[0]+40,bloodalterrect[1]+50)).leftrand()
                    time.sleep(3)
                elif playerPosR==pos10:
                    if first == white:
                        print('click on blood alter')
                        Mouse((bloodalterrect[0]+20,bloodalterrect[1]+30),(bloodalterrect[0]+40,bloodalterrect[1]+50)).leftrand()
                        cantchisel = False
                        time.sleep(1)
                    elif first == bagcolor and lastslot == bagcolor:
                        print('find climb 2 and switch cantchiesel to False')
                        cantchisel = False
                        Mouse((climb2rect[0]+5,climb2rect[1]+36),(climb2rect[0]+13,climb2rect[1]+38)).leftrand()
                        time.sleep(4)
                    else:
                        cantchisel = False


            elif first == white and lastslot == yellow:        
                
                if playerPosD == pos2:
                    print("Pos2 (50,255,0)\n")
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                #pos3
                elif playerPosU == pos3:
                    print("Pos3 (51,255,0)\n")
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                #pos4
                elif playerPosL == pos4:
                    print("Pos4 (52,255,0)\n")
                    Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                    time.sleep(.5)
                elif playerPosU == pos6:
                    print("Pos6 (54,255,0)\n")
                    Mouse((darkalterrect[0]+10,darkalterrect[1]+10),(darkalterrect[0]+30,darkalterrect[1]+30)).leftrand()
                    time.sleep(.5)
                elif playerPosR == pos7:
                    if lastslot == red:
                        print('heading to blood alter...')
                        Mouse((1588,171),(1590,172)).leftrand()
                        time.sleep(.5)
                elif playerPosD == pos9:
                    print('Youve made it to pos9 click on blood alter...')
                    Mouse((bloodalterrect[0]+20,bloodalterrect[1]+30),(bloodalterrect[0]+40,bloodalterrect[1]+50)).leftrand()
                    time.sleep(3)
                else:
                    print(f'routing... c={cantchisel}m={mining}b={bagfull}')
                    
            elif lastslot == red:
                if playerPosR == pos7:
                    print('Heading to pos9 cant chisel....')
                    Mouse((1588,171),(1590,172)).leftrand()
                    time.sleep(.5)

                elif playerPosL == pos9:
                    print('Youve made it to pos9 click on blood alter...')
                    Mouse((bloodalterrect[0]+20,bloodalterrect[1]+30),(bloodalterrect[0]+40,bloodalterrect[1]+50)).leftrand()
                    time.sleep(3)
                elif playerPosR == pos10:
                    print(f'chiseling... c={cantchisel}')
                    chiseling()
                else:    
                    print(f'routing... c={cantchisel}b={bagfull}')
            elif first == white and lastslot == bagcolor:
                if playerPosR ==pos10:
                    print(f'click on blood alter... c=(cantchisel)')
            else:    
                print(f'routing... c={cantchisel}b={bagfull}')
        
        
        #bag full and cant chisel
        else:
            if playerPosD == pos2:
                print("Pos2 (50,255,0)\n")
                Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                time.sleep(.5)
            #pos3
            elif playerPosU == pos3:
                print("Pos3 (51,255,0)\n")
                Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                time.sleep(.5)
            #pos4
            elif playerPosL == pos4:
                print("Pos4 (52,255,0)\n")
                Mouse((climb1rect[0]+15,climb1rect[1]+15),(climb1rect[0]+19,climb1rect[1]+20)).leftrand()
                time.sleep(.5)
            elif playerPosU == pos6:
                print(f'go to dark alter... c={cantchisel} ,b{bagfull}')
                Mouse((1588,171),(1590,172)).leftrand()
                time.sleep(2)
            elif playerPosR == pos7:
                print('heading to blood alter...')
                Mouse((1588,171),(1590,172)).leftrand()
                cantchisel = False
                time.sleep(.5)
            else:
                print(f'c={cantchisel},b={bagfull}')  
            
            
            if playerPosD == pos9:
                print('Youve made it to pos9 click on blood alter...')
                Mouse((bloodalterrect[0]+20,bloodalterrect[1]+30),(bloodalterrect[0]+40,bloodalterrect[1]+50)).leftrand()
                time.sleep(3)
            elif playerPosR == pos10:
                if lastslot == red:
                    print("start chiseling....")
                    chiseling()
                    time.sleep(1)
                elif first == white and lastslot == bagcolor:
                    print('click on blood alter')
                    Mouse((bloodalterrect[0]+20,bloodalterrect[1]+30),(bloodalterrect[0]+40,bloodalterrect[1]+50)).leftrand()
                    cantchisel = False
                    time.sleep(1)
                elif first == bagcolor and lastslot == bagcolor:
                    print('find climb 2 and switch cantchiesel to False')
                    cantchisel = False
                    Mouse((climb2rect[0]+5,climb2rect[1]+36),(climb2rect[0]+13,climb2rect[1]+38)).leftrand()
                    time.sleep(4)
            else:
                print(f'c={cantchisel},b={bagfull}')"""