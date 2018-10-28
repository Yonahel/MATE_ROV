#Client side of architecture

#TODO: Initialize as client
#TODO: Send controller data to Pi
#TODO: Possibly receive data from Pi (TBD)

# echo_client.py
import socket

def getControllerInput():
	#replace with function to recieve input from controller
	cInput = raw_input("controller input: ")
	return cInput

host = socket.gethostname()

port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
	s.sendall(getControllerInput())
	data = s.recv(1024)
	print('Received', repr(data))

s.close()




