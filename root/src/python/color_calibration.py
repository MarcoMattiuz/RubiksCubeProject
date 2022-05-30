
from pickle import NONE
from attr import NOTHING
import cv2 


class Color_Calibration:

    def color_tracker():
        cv2.namedWindow("trackbars")
        cv2.createTrackbar("White","trackbars",0,100,lambda x:x)
        cv2.createTrackbar("Red","trackbars",0,255,lambda x:x)
        cv2.createTrackbar("Green","trackbars",0,255,lambda x:x)
        cv2.createTrackbar("Blue","trackbars",0,255,lambda x:x)
        cv2.createTrackbar("Orange","trackbars",0,255,lambda x:x)
        cv2.createTrackbar("Yellow","trackbars",0,255,lambda x:x)
        cv2.setTrackbarPos("White","trackbars",80)
        cv2.setTrackbarPos("Red","trackbars",5)
        cv2.setTrackbarPos("Orange","trackbars",22)
        cv2.setTrackbarPos("Yellow","trackbars",58)
        cv2.setTrackbarPos("Green","trackbars",78)
        cv2.setTrackbarPos("Blue","trackbars",131)

    def get_color_name(hsv):
        
        saturation_value = hsv[1]
        hue_value = hsv[0]

        color = "Undefined"
      
        if saturation_value<cv2.getTrackbarPos("White","trackbars"):
            color = "WHITE"
        elif hue_value < cv2.getTrackbarPos("Red","trackbars") :
            color = "RED"
        elif hue_value < cv2.getTrackbarPos("Orange","trackbars"):
            color = "ORANGE"
        elif hue_value < cv2.getTrackbarPos("Yellow","trackbars"):
            color = "YELLOW"
        elif hue_value < cv2.getTrackbarPos("Green","trackbars"):
            color = "GREEN"
        elif hue_value < cv2.getTrackbarPos("Blue","trackbars"):
            color = "BLUE"   
        else:
            color = "RED"      

        return color    
    