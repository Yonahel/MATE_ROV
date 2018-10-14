#Server running on Raspberry Pi controlling everything

#TODO: Initialize as server
#TODO: Receive controller data from laptop

import socket

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

# establish a connection and waiting...
conn, addr = s.accept()
print('Connected by', addr)

while True:
    # Receive no more than 1024 bytes
    data = conn.recv(1024)
    print(data)
    if not data:
        break
    conn.sendall(data)

conn.close()
