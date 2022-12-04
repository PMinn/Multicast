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

print("S")

group = (MULTICAST_GROUP1, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.2)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

@eel.expose
def send(message):
	print(message)
	sock.sendto(str(message).encode('utf-8'), group)
	eel.writeMsg(0,f"{message}, MULTICAST to {group[0]}:{str(group[1])}")

eel.start('S.html', size=(500, 500),port=0)
# sock.close()