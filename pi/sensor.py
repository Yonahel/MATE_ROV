#Read sensor data from Arduino via Serial
import serial
import time

#Initialize Serial Connection with Arduino
PORT = "/dev/ttyACM0"

ser=serial.Serial(PORT,9600)  
ser.baudrate=9600
i = 0

#Read Serial Data
while True:
	while !i:
		i = port.read(1)
	accel_x = port.read(16)
	accel_y = port.read(16)
	accel_z = port.read(16)
	imu_roll = port.read(16)
	imu_pitch = port.read(16)
	imu_yaw = port.read(16)

#TODO: Data filter, process, etc


#TODO: Pass data to PID (done over ROS)
