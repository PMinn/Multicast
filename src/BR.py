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

print("BR")

def joinGroup(s, group_addr):
	group = socket.inet_aton(group_addr)
	mreq = struct.pack('4sL', group, socket.INADDR_ANY)
	s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

def leaveGroup(s, group_addr):
	group = socket.inet_aton(group_addr)
	mreq = struct.pack('4sL', group, socket.INADDR_ANY)
	s.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)

TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
TCPSocket.bind((TCP_IP, TCP_PORT))
TCPSocket.listen(backlog)
client, (rip, rport) = TCPSocket.accept()
eel.writeMsg(2,f"connect from {rip}:{str(rport)}")

recvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
recvSocket.bind(('', PORT))

joinGroup(recvSocket, MULTICAST_GROUP1)
eel.writeMsg(2,f"join multicast group {MULTICAST_GROUP1}:{str(PORT)}")
print('Listening on multicast group (%s, %d)' % (MULTICAST_GROUP1, PORT))

threading.Thread(target=lambda:eel.start('BR.html', size=(500, 500),port=0)).start()

while 1:
	data, rAddr = recvSocket.recvfrom(BUFF_SIZE)
	eel.writeMsg(1, f"{data.decode('utf-8')} ,MULTICAST from {str(rAddr[0])}:{str(rAddr[1])}")
	client.send(data)
	eel.writeMsg(0, f"{data.decode('utf-8')} ,TCP from {TCP_IP}:{str(TCP_PORT)} to {rip}:{str(rport)}")

# leaveGroup(recvSocket, MULTICAST_GROUP1)
# recvSocket.close()