####################################################
#  D1014636 潘子珉
####################################################
import threading
import socket
import struct
import eel
eel.init('gui', allowed_extensions=['.js', '.html'])

backlog = 5
BUFF_SIZE = 1024

MULTICAST_GROUP1 = '225.9.9.9'
MULTICAST_GROUP2 = '225.10.10.10'
PORT = 6666

TCP_IP = "127.0.0.1"
TCP_PORT = 8888

print("C")

def joinGroup(s, group_addr):
	group = socket.inet_aton(group_addr)
	mreq = struct.pack('4sL', group, socket.INADDR_ANY)
	s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

def leaveGroup(s, group_addr):
	group = socket.inet_aton(group_addr)
	mreq = struct.pack('4sL', group, socket.INADDR_ANY)
	s.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)

recvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
recvSocket.bind(('', PORT))

joinGroup(recvSocket, MULTICAST_GROUP2)
print('Listening on multicast group (%s, %d)' % (MULTICAST_GROUP2, PORT))

threading.Thread(target=lambda:eel.start('C.html', size=(500, 500),port=0)).start()

while 1:
	data, (rip, rport) = recvSocket.recvfrom(BUFF_SIZE)
	# print(f"Receive messgae: {data.decode('utf-8')},from IP: {str(rip)} port: {str(rport)}")
	eel.writeMsg(1, f"{data.decode('utf-8')} ,MULTICAST from {str(rip)}:{str(rport)}")
	
leaveGroup(recvSocket, MULTICAST_GROUP2)
recvSocket.close()