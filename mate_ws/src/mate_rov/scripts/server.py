#Server running on Raspberry Pi controlling everything

#TODO: Initialize as server
#TODO: Receive controller data from laptop

import rospy
import socket
import motor.msg
import w_data.msg

#callback for the subscriber
def get_w_data(conn, data):
	rospy.loginfo(data)
    transformed_data = "!("+data.temp+","+data.ph+")^"
	conn.sendall(transformed_data)

#creating websocket to connect to client/GUI
host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

#initialize publisher/subscriber
motor_topic = rospy.Publisher('motor', motor.msg ,queue_size = 10)
w_data_sub = rospy.Subscriber('w_data', w_data.msg , get_w_data(conn, data))
rospy.init_node('server', anonymous=True)
rate = rospy.Rate(50)
rospy.spinOnce()

#loop to publish any motor commands recieved.
while not rospy.is_shutdown():
    motor_cmd = conn.recv(1024)
    rospy.loginfo(motor_cmd)
    
    if motor_cmd[0] == $
        #transform function is: $(Int,Int),(Int,Int)% => int8[2]
        motor_cmd.strip(")").strip("(").strip("$").strip("%")
        cmd_list = motor_cmd.split(",")
        #TO-DO: cmd_list of 4 ints => int8[2] motor.msg
        motor_topic.publish(motor_cmd) #?
        rate.sleep()

conn.close()
