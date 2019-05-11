#Client to transfer data from compupter to Pi
#Client hosted on computer

import socket
import rospy
import roslib
from mate_rov.msg import Control


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 7776        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

def callback(data)
        joyStickLeftX = str(data.LEFTX)
        joyStickLeftY = str(data.LEFTY)
        joyStickRightX = str(data.RIGHTX)
        joyStickRightY = str(data.RIGHTY)

        msg = str('<' + joyStickLeftX + ' ' + joyStickLeftY + ' ' + joyStickRightX + ' ' + joyStickRightY + '>' + '\n')

        s.sendall(msg.encode())

rospy.init_node('data_client', anonymous=True)
 
rospy.Subscriber("controller_topic", Control, callback)
 
# spin() simply keeps python from exiting until this node is stopped
rospy.spin()
