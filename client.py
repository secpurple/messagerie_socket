import os
import socket 
from scapy.all import Ether, IP # pip install scappy

def message():
	message = input(" > : ")
	send_message = ("""
----------------------------------
| envoyer par : """+hostname+""" 
| addr_IPv4 / """+ip+"""      
| addr_MAC / """+mac+"""      
----------------------------------
| => """+message)
	client.send(send_message.encode('utf-8'))
	if reponse == "fin":
		print('le server a couppé la comunication ! ')
		client.close()

os.system('clear')
hostname = socket.gethostname()
host = '192.168.0.101'
port = 1024
ip = IP(dst="0.0.0.0").src
mac = Ether().src
client = socket.socket()
server = client.connect((host, port))
print(server)
client.send('bon'.encode('utf-8'))
reponse = client.recv(255).decode("utf-8")
print(reponse)

message()
