#Client which receives video content

import socket
import numpy as np
import cv2

UDP_IP = '127.0.0.1'                  
UDP_PORT = 999        
cap = cv2.VideoCapture(0)

xImgSize = 640    #Change depending on camera resolution
yImgSize = 480    #Change depending on camera resolution
msg_size = xImgSize*yImgSize*3

while(True):
   ret, frame = cap.read()
   cv2.imshow('frame',frame)
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   d = frame.flatten ()
   s = d.tostring ()
   for i in xrange(20):
       sock.sendto (s[i*(msg_size/20):(i+1)*(msg_size/20)],(UDP_IP, UDP_PORT))


        if cv2.waitKey(1) & 0xFF == ord('q'):
          break

cap.release()
cv2.destroyAllWindows()
