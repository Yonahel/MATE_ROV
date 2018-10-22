#TODO: Receive data from PID (done over ROS)
#TODO: Initialize GPIO
#TODO: Send data over TX/RX to Arduino
#TODO: Receive sensor data from Arduino


import math
from pid import PID

multiplier = 1
motor = dict.fromkeys(["frontLeft", "frontRight", "backLeft", "backRight", "front", "back", "left", "right"], 0)

def remoteControl(j1x, j1y, j2x, j2y, btnL1, btnL2, btnR1, btnR2):
        # one joystick control
        # 2 sticks (4 planes), 4 buttons, tentative mapping
        # j prefixes refer to sticks with values -127 to 127, btn prefix refers to buttons for True or False.

        # xy movement
		motor[frontLeft] = j1y + j1x + j2x;
		motor[frontRight] = j1y - j1x - j2x;
		motor[backLeft] = j1y - j1x + j2x;
		motor[backRight] = j1y + j1x - j2x;
        if(btnL1): # pitch left
                motor[left] = -127 * multiplier
                motor[right] = 127 * multiplier
                motor[front] = 0
                motor[back] = 0
        elif(btnR1): # pitch right
                motor[left] = 127 * multiplier
                motor[right] = -127 * multiplier
                motor[front] = 0
                motor[back] = 0
        elif(btnL2): # dive
                motor[front] = -127 * multiplier
                motor[back] = -127 * multiplier
                motor[left] = -127 * multiplier
                motor[right] = -127 * multiplier
        elif(btnR2): # rise
                motor[front] = 127 * multiplier
                motor[back] = 127 * multiplier
                motor[left] = 127 * multiplier
                motor[right] = 127 * multiplier
        else: # roll forward/back using joystick
            motor[front] = -j2y
            motor[back] = j2y
            motor[left] = 0
            motor[right] = 0

def preMove(xy_power=0, xy_angle=0, z_power=0, roll_power=0, pitch_power=0, yaw_power=0):
    # handles [(xy_power, xy_angle) XOR (yaw)] OR/AND [(roll, pitch) XOR (z)] simultaneously
    if(xy_power != 0):
        x = math.sin(xy_angle) * xy_power;
    	y = math.cos(xy_angle) * xy_power;
    	motor[frontLeft] = y + x;
    	motor[frontRight] = y - x;
    	motor[backLeft] = y - x;
    	motor[backRight] = y + x;

    if(z != 0)
        motor[front] = -z_power
        motor[back] = -z_power
        motor[left] = -z_power
        motor[right] = -z_power

    if(roll_power != 0 or pitch_power != 0):
        motor[front] = -roll_power
        motor[back] = roll_power
        motor[left] = pitch_power
        motor[right] = -pitch_power

    if(yaw_power != 0)
        motor[frontLeft] = yaw_power
    	motor[frontRight] = -yaw_power
    	motor[backLeft] = yaw_power
    	motor[backRight] = -yaw_power

def pidControl(sensor_r, sensor_y, sensor_p, rP, rI, rD, pP, pI, pD, yP, yI, yD, setPoint=0.0, sampleTime=0.1):
    roll_pid = PID(rP, rI, rD)
    pitch_pid = PID(pP, pI, pD)
    yaw_pid = PID(yP, yI, yD)

    roll_pid.setPoint = setPoint
    pitch_pid.setPoint = setPoint
    yaw_pid.setPoint = setPoint

    roll_pid.setSampleTime(sampleTime)
    pitch_pid.setSampleTime(sampleTime)
    yaw_pid.setSampleTime(sampleTime)

    while(True):
        roll_pid.update(sensor_r)
        pitch_pid.update(sensor_p)
        yaw_pid.update(sensor_y)
        preMove(roll_power = roll_pid.output, pitch_power = pitch_pid.output, yaw_pid = yaw_pid.output)

    #TODO: add funcitonality to change setPoint while in loop


def output():
    #TODO: send motor value to arduino [FL, FR, BL, BR, F, B, L, R] OVER TX/RX
