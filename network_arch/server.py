#Server running on Raspberry Pi controlling everything

#TODO: Initialize as server
#TODO: Receive controller data from laptop

'''
    Simple socket server using threads
'''
 
import socket
import threading
import sys
 
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = ''   # Symbolic name, meaning all available interfaces
        self.port = port # Arbitrary non-privileged port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print 'Socket created'

        #Bind socket to local host and port
        try:
    		self.sock.bind((self.host, self.port))
        except socket.error as msg:
    		print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    		sys.exit()
     	print 'Socket bind complete'

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
    	clientName = address[0] + ':' + str(address[1])
        print 'Connected with ' + str(clientName)  + '!'
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data 
                    response = data
                    client.send(response)
                else:
                    raise error('Client disconnected')
            except:
            	print str(clientName) + ' has disconnected!'
                client.close()
                return False
 
if __name__ == "__main__":
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()