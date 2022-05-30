import cv2
from color_detect import Color_Detect as cd
from color_calibration import Color_Calibration as cc
import numpy as np
from sendString import SendString as sendString

#import kociemba 
cap  = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
colorR = [180,180,180]
face = ['WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE', 'WHITE']
cube = []*6
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
    
    key = cv2.waitKey(1)
    if(key==32):
        spaceBar=True
        cube.append(face[:])
        if cubeface<6:
          cubeface += 1
        else:
          sendString.sendString("FDDD'F'L2LDDBBR")
          cubeface = 0  
          cube.clear()
        print("cube",cube)

    cv2.imshow("Frame",frame)
    
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