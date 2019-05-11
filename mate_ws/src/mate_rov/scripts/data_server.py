#Server to transfer data from computer to Pi
#server hosted on pi

import rospy
import roslib
from mate_rov.msg import Control
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 7776        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)

        pub = rospy.Publisher('data_server', Control, queue_size=10)
        rospy.init_node('motor_topic', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        
        while not rospy.is_shutdown():
            #Receive data from client, decode
            data = conn.recv(1024)
            msg = data.decode()
            
            #Delimit string, get string array of values
            joyStickPos = data.split('<> ')
               
            msg = Control()
            msg.LEFTX = joystickPos[0]
            msg.LEFTY = joystickPos[1]
            msg.RIGHTX = joystickPos[2]
            msg.RIGHTY = joystickPos[3]

            #Pass along to motor function
            pub.publish(msg)
            rate.sleep()
            
            if not data:    
                break

            
