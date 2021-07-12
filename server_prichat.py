import socket
import threading
import os
from colorama import init
from colorama import Fore,init
from colorama import Back,init

os.system('clear')
os.system('ifconfig')
host = input('> ')
port = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()
print (Back.GREEN + f"Servidor Activo en {host}:{port}")
print (Back.BLACK)
clients = []
usernames = []

def broadcast(message, _client):
	for client in clients:
		if client != _client:
			client.send(message)

def handle_messages(client):
	while True:

		try:
			message = client.recv(1024)
			broadcast(message, client)
		except:
			index = clients.index(client)
			username = usernames[index]
			print (Back.RED + Fore.WHITE)
			broadcast(f"PriChat: {username} se desconectó".encode('utf-8'))
			print (Back.BLACK + Fore.WHITE)
			clients.remove(client)
			usernames.remove(username)
			client.close()
			break

def receive_connections():
	while True:

		client, address = server.accept()
		print (Back.RED + Fore.YELLOW)
		client.send("@username".encode('utf-8'))
		username = client.recv(1024).decode('utf-8')
		print (Back.BLACK + Fore.WHITE)
		clients.append(client)
		usernames.append(username)

		print (Back.GREEN + f"{username} se conectó al chat como {str(address)}")
		print (Back.BLACK)

		message = f"PriChat: {username} esta dentro del chat".encode('utf-8')
		broadcast(message,client)
		client.send("Conectado al servidor".encode('utf-8'))
		thread = threading.Thread(target=handle_messages, args=(client,))
		thread.start()

receive_connections()
