#Receives motor data from PID, sends to Arduino

#TODO: Receive data from PID (done over ROS)
#TODO: Filter and process data to format easy for Arduino
#TODO: Initialize GPIO
#TODO: Send data over TX/RX to Arduino

min_speed = -127 # backwards
max_speed = 127 # forwards

##################
# BASE FUNCTIONS #
##################

def move_xy(power=max_speed, angle=0):
    pass

def move_z(power=max_speed):
    pass

def roll(power=max_speed):
    pass

def pitch(power=max_speed):
    pass

def rotate(power=max_speed):
    pass

def yaw(power=max_speed): # if preferred
    rotate(power)

#################
# SUPPLEMENTALS #
#################

def roll_deg(power=max_speed, angle):
    pass

def pitch_deg(power=max_speed, angle):
    pass

def move_z_fixed(power=max_speed, distance):
    pass

def move_xy_fixed(power=max_speed, distance):
    pass

def rotate_deg(power=max_speed, angle):
    pass
