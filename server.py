#######################################
## BY : https://github.com/secpurple ##
## date : 05 april 2022              ##
## sript : server                    ##
#######################################
import os
import socket

	
def message():
	message = input(' > : ')
	message_send = ("""
----------------------------------
| envoyer par : server           |
----------------------------------
| => """+message ) 
	client.send(message_send.encode("utf-8"))
	reponse = client.recv(255).decode('utf-8')
	print(reponse)
	if reponse == "fin":
		client.close()

os.system('clear')
host = ''
port = 1024
server = socket.socket()
print('serveur lancer')
server.bind((host, port))
server.listen(3)
print("server ecoute sur le port ", port)
client, addr = server.accept()
print("connection sur : ", addr )
reponse = client.recv(255).decode('utf-8')
print(reponse)

message()
