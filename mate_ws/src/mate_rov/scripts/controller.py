import pygame
import time
import rospy
import roslib
from mate_rov.msg import Control


"""

        LY -1                         RY    -1

LX -1               1           RX -1            1  

            1                            1


"""
#Joystick initialization
pygame.init()
pygame.joystick.init()

joy = pygame.joystick.Joystick(0)
joy.init()

while True:
    #Required
    pygame.event.pump()

    pub = rospy.Publisher('controller_topic', Control, queue_size=10)
    rospy.init_node('controller_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = Control() 
        msg.LEFTX = joy.get_axis(0)
        msg.LEFTY = joy.get_axis(1)
        msg.RIGHTX = joy.get_axis(4)
        msg.RIGHTY = joy.get_axis(3)

        pub.publish(msg)
        rate.sleep()
