import cv2
import sys
cpt = 0

vidStream = cv2.VideoCapture(0)
while True:
    
    ret, frame = vidStream.read() # read frame and return code.
    
    cv2.imshow("test window", frame) # show image in window
    
     cv2.imwrite(r"C:/Users/pywiz/Desktop/facce recgonizations/train-images/0/image%04i.jpg" %cpt, frame)    
    cpt += 1
    
        

    if cv2.waitKey(10)==ord('s'):
        break
        

