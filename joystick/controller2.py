import pygame

#Joystick initialization
pygame.init()
pygame.joystick.init()

joy = pygame.joystick.Joystick(0);
joy.init()

while True:
    #Designated axes -> leftX - 1, leftY - 2, rightX - 3, rightY -4
    leftX = joy.get_axis(0);
    leftY = joy.get_axis(1):
    rightX = joy.get_axis(2);
    rightY = joy.get_axis(3);

    #Send message (ROS)
    

