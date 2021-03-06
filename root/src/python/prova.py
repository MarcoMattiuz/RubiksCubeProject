from ntpath import join
import cv2
from color_detect import Color_Detect as cd
from color_calibration import Color_Calibration as cc
import numpy as np
from sendString import SendString as sendString
from code_solver import cubeSolver
#import kociemba 
cap  = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
colorR = [180,180,180]
face = ['WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE']
cube = []*6
#cube = [['WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE'],
       # ['GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN', 'GREEN'],
       # ['YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW', 'YELLOW'],
       # ['ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE', 'ORANGE'],
       # ['RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED', 'RED'],
       # ['BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE', 'BLUE']]
spaceBar = False
cubeface = 0
cc.color_tracker()

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height,width,_ = frame.shape 

    cx = int(width/2)
    cy = int(height/2)

    if spaceBar==True:
        for index,x in enumerate(cube):
          cd.draw_current_cubes(frame,cube[index],cubeface)
      
    cd.draw_detecting_stickers(frame,face)
    for index,(x,y) in enumerate(cd.get_detection_stickers()):
        roi = hsv_frame[y:y+50,x:x+50]
        avg_hsv = cd.median_hsv(roi)
        color_name = cc.get_color_name(avg_hsv)
        face[index] = color_name

    frame = cv2.flip(frame, 1)
    
    #SPACEBAR key to append a new face to the cube array 
    key = cv2.waitKey(1) 

    if(key==32):
        spaceBar=True

        if cubeface<6:         
          cube.append(face[:])
          cubeface += 1
        else:
          #sendString.sendString("FBFRDDB")
          cB = cubeSolver(cube)
          cB.D_move()
          print("after D-move", cube)
          cB.F_move()
          print("after LI-move", cube)
          cB.R_move()
          print("after D-move", cube)
          cB.FI_move()
          print("after LI-move", cube)
          cB.D_move()
          print("after D-move", cube)
          ####---
          cB.LI_move()
          print("after LI-move", cube)
          cB.BI_move()

          cB = cubeSolver(cube)
         
     
          cubeface = 0  
          cube = []*6
        print("cube",cube)

    cv2.imshow("Frame",frame)
    #ESC key to exit program
    if key==27: 
        break

    """         
                    -----
                  | G G G |
                  | G G G | 
                  | G G G |
                    -----
                  | Y Y Y |
                  | Y Y Y |
                  | Y Y Y |
            -----   -----   ----- 
          | R R R | B B B | O O O | 
          | R R R | B B B | O O O | 
          | R R R | B B B | O O O | 
            -----   -----   -----   
                  | W W W |
                  | W W W |
                  | W W W |
                    -----
    """   
    #li2 = [ y for x in cube for y in x]
    #','.join(map(str,li2))
cap.release()
cv2.destroyAllWindows()