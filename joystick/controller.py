import pygame
import time

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

    #Designated axes -> leftX - 1, leftY - 2, rightX - 3, rightY -4
    leftX = joy.get_axis(0)
    leftY = joy.get_axis(1)
    rightX = joy.get_axis(4)
    rightY = joy.get_axis(3)

    #Send message (ROS or IPC, still deciding)
    time.sleep(.2)   
