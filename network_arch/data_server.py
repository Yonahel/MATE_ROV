#Server to transfer data from computer to Pi
#server hosted on pi

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 7776        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            #Receive data from client, decode
            data = conn.recv(1024)
            msg = data.decode()
            
            #Delimit string, get string array of values
            joyStickPos = data.split('<> ')

            #Pass along to motor function (ROS or IPC)

            
            if not data:
                break

            
