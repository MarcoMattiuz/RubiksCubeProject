
import cv2
import numpy as np
state   = [ 0,0,0,                       # current sticker colors
            0,0,0,
            0,0,0 ]
facePos = 0

current_stickers = [[150, 200], [180, 200], [210, 200],
                    [150, 230], [180, 230], [210, 230],
                    [150, 260], [180, 260], [210, 260]]

cubePos = [[0,0], [0, -100], [0,-200],
     [100,0], [-100,0], [0,100]]

detection_stickers = [[530, 250], [630,250], [730,250],
                [530, 350], [630,350], [730,350],
                [530, 450], [630,450], [730,450]]

class Color_Detect:

    def draw_current_cubes(frame,color,count):
        global facePos
        
        if facePos<count:
            Color_Detect.draw_current_stickers(frame,color,cubePos[facePos])
            facePos = (facePos+1)%count
      
       

    def draw_current_stickers(frame,color,ds1):
        i=0 
        for index in current_stickers:
            bgr_color = Color_Detect.color_to_bgr(color[i])
            i+=1
            cv2.rectangle(frame,(index[0]+ds1[0],index[1]+ds1[1]),(index[0]+25+ds1[0],index[1]+25+ds1[1]),bgr_color,-1)


    def draw_detecting_stickers(frame,colorArr):
        i=0
        for index in detection_stickers:
            bgr_color = Color_Detect.color_to_bgr(colorArr[i])
            i+=1
            cv2.rectangle(frame,index,(index[0]+50,index[1]+50),bgr_color,-1)

    def get_detection_stickers():
        return detection_stickers
    
    def get_current_stickers():
        return current_stickers

    def median_hsv(roi):
        """ Average the HSV colors in a region of interest.
        :param roi: the image array
        :returns: tuple
        """    
        h = []
        s = []
        v = []
        num = 0
    
        for y in range(len(roi)):
            if y % 10 == 0:
                 for x in range(len(roi[y])):
                    if x % 10 == 0:
                        chunk = roi[y][x]
                        num += 1
                        h.append(chunk[0])
                        s.append(chunk[1])
                        v.append(chunk[2])
                    
        return (int(np.median(h)), int(np.median(s)), int(np.median(v))) 
    
    def color_to_bgr(color_name):

        color1 = {
            'RED'    : (0,0,255),
            'ORANGE' : (0,165,255),
            'BLUE'   : (255,0,0),
            'GREEN'  : (0,255,0),
            'WHITE'  : (255,255,255),
            'YELLOW' : (0,255,255)
        }

        return color1[color_name]
