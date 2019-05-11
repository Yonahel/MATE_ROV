import socket
import numpy
import time
import cv2

UDP_IP="127.0.0.1"
UDP_PORT = 999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

xImgSize = 640
yImgSize = 480
msg_size = (640 * 480 * 3) / 20

s=""

while True:
      data, addr = sock.recvfrom(msg_size)
      s+= data
      if len(s) == (msg_size*20):
          frame = numpy.fromstring (s, dtype=numpy.uint8)
          frame = frame.reshape(480,640,3)
          cv2.imshow("frame",frame)

          s=""
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
