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

print("BC")

TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

group = (MULTICAST_GROUP2, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.2)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

threading.Thread(target=lambda:eel.start('BC.html', size=(500, 500),port=0)).start()

try:
	TCPSocket.connect((TCP_IP, TCP_PORT))
	eel.writeMsg(2,f"connect to {TCP_IP}:{str(TCP_PORT)}")
except Exception as msg:
	print(f"error:{msg}")
	eel.writeMsg(4,str(msg))
else:
	while 1:
		data = TCPSocket.recv(BUFF_SIZE)
		eel.writeMsg(1,f"{data.decode('utf-8')} TCP from {TCP_IP}:{str(TCP_PORT)}")
		sock.sendto(data, group)
		eel.writeMsg(0,f"{data.decode('utf-8')} MULTICAST to {group[0]}:{str(group[1])} ")
	# sock.close()