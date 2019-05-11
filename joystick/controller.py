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

last_LX = 0
last_LY = 0
last_RX = 0
last_RY = 0


while True:
    #Required
    pygame.event.pump()

    #Designated axes -> leftX - 1, leftY - 2, rightX - 3, rightY -4
    leftX = joy.get_axis(0)
    leftY = joy.get_axis(1)
    rightX = joy.get_axis(4)
    rightY = joy.get_axis(3)

    #Send message (ROS or IPC, still deciding)
    if( leftX != last_LX or
        leftY != last_LY or
        rightX != last_RX or
        rightY != last_RY ):
        print ("LEFT X " + str(leftX))
        print ("LEFT Y " + str(leftY))
        print ("RIGHT X " + str(rightX))
        print ("RIGHT Y " + str(rightY))
    time.sleep(.2)   
    last_LX = leftX
    last_LY = leftY
    last_RX = rightX
    last_RY = rightY