#Code for the MATE ROV motor control
#This code receives motions from a joystick, converts them to ESC speed values, and sends them to an Arduino

import rospy
import roslib
import serial
from mate_rov.msg import Control

port = 'dev/ttyACM0'
motorSpeed = 0;

arduino = serial.Serial(port,115200,timeout=25)

def callback(data):
    #Joysticks will work as follows :
    #Left joystick controls forward, back, right, left
    #Right joystick controls up and down
    #Turn around using right joystick sides
    #No yaw pitch roll control for now

    time.sleep(0.05) #Nick does it, so do I ;)

    #Get value from joystick function here
    leftJoystickX = data.LEFTX
    leftJoystickY = data.LEFTY
    rightJoystickX = data.RIGHTX
    rightJoystickY = data.RIGHTY

    #Joystick values range from -1 to 1, ESC ranges from 1150 - 1500 (needs testing, as well as tweaking)
    default = 1300
    delta = 150         #Needs testing


    i1speed = str(default)
    i2speed = str(default)
    i3speed = str(default)
    i4speed = str(default)
    o1speed = str(default)
    o2speed = str(default)
    o3speed = str(default)
    o4speed = str(default)


    #Left joystick left
    if(leftJoystickX < 0)
        #I1, I3 forward, I2, I4 reverse
        i1speed = str(default +- (delta * leftJoystickX))
        i2speed = str(default +- (delta * leftJoystickX))
        i3speed = str(default +- (delta * leftJoystickX))
        i4speed = str(default +- (delta * leftJoystickX))
    #Left joystick right
    elif(leftJoystickX > 0)
        #I2, I4 forward, I1, I3 reverse
        i1speed = str(default +- (delta * leftJoystickX))
        i2speed = str(default +- (delta * leftJoystickX))
        i3speed = str(default +- (delta * leftJoystickX))
        i4speed = str(default +- (delta * leftJoystickX))
    #Left joystick down
    if(leftJoystickY < 0)
        #I3, I4 forward, I1, I2 back
        i1speed = str(default +- (delta * leftJoystickY))
        i2speed = str(default +- (delta * leftJoystickY))
        i3speed = str(default +- (delta * leftJoystickY))
        i4speed = str(default +- (delta * leftJoystickY))
    #Left joystick up
    elif(leftJoystickY > 0)
        #I1, I2 forward, I3, I4 back
        i1speed = str(default +- (delta * leftJoystickY))
        i2speed = str(default +- (delta * leftJoystickY))
        i3speed = str(default +- (delta * leftJoystickY))
        i4speed = str(default +- (delta * leftJoystickY))
    #Right joystick down
    if(rightJoystickY < 0)
        #O1, O2, O3, O4 back
        o1speed = str(default +- (delta * rightJoystickY))
        o2speed = str(default +- (delta * rightJoystickY))
        o3speed = str(default +- (delta * rightJoystickY))
        o4speed = str(default +- (delta * rightJoystickY))
    #Right joystick up
    elif(rightJoystickY > 0)
        #O1, O2, O3, O4 forward
        o1speed = str(default +- (delta * rightJoystickY))
        o2speed = str(default +- (delta * rightJoystickY))
        o3speed = str(default +- (delta * rightJoystickY))
        o4speed = str(default +- (delta * rightJoystickY))
    #Right joystick left
    if(rightJoystickX < 0)
        #I* forward
        i1speed = str(default +- (delta * rightJoystickX))
        i2speed = str(default +- (delta * rightJoystickX))
        i3speed = str(default +- (delta * rightJoystickX))
        i4speed = str(default +- (delta * rightJoystickX))
    #Right joystick right
    elif(rightJoystickX > 0)
        #I* back
        i1speed = str(default +- (delta * rightJoystickX))
        i2speed = str(default +- (delta * rightJoystickX))
        i3speed = str(default +- (delta * rightJoystickX))
        i4speed = str(default +- (delta * rightJoystickX))
    
    arduino.write(bytes("I1" + ' ' + i1speed + '\n','ASCII')) 
    arduino.write(bytes("I2" + ' ' + i2speed + '\n','ASCII')) 
    arduino.write(bytes("I3" + ' ' + i3speed + '\n','ASCII')) 
    arduino.write(bytes("I4" + ' ' + i4speed + '\n','ASCII')) 
    
    arduino.write(bytes("O1" + ' ' + o1speed + '\n','ASCII')) 
    arduino.write(bytes("O2" + ' ' + o2speed + '\n','ASCII')) 
    arduino.write(bytes("O3" + ' ' + o3speed + '\n','ASCII')) 
    arduino.write(bytes("O4" + ' ' + o4speed + '\n','ASCII')) 

rospy.init_node('motor_node', anonymous=True)

rospy.Subscriber("motor_topic", Control, callback)

# spin() simply keeps python from exiting until this node is stopped
rospy.spin()
