#Client to transfer data from compupter to Pi
#Client hosted on computer

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 7776        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:

        joyStickLeftX = str()
        joyStickLeftY = str()
        joyStickRightX = str()
        joyStickRightY = str()

        msg = str('<' + joyStickLeftX + ' ' + joyStickLeftY + ' ' + joyStickRightX + ' ' + joyStickRightY + '>' + '\n')

        s.sendall(msg.encode())

print('Received', repr(data))
