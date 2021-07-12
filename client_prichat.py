import os
import socket
import threading
from colorama import init
from colorama import Fore,init
from colorama import Back,init
							
username = input(Back.WHITE + Fore.BLACK + "Ingresa tu nombre de usuario: ")
			
host = input('> ')
port = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive_messages():
	while True:
		try:
			message = client.recv(1024).decode('utf-8')

			if message == "@username":
				client.send(username.encode('utf-8'))
				print (Back.BLACK + Fore.WHITE)
			else:
				print (message)
		except:
			print (Back.RED + Fore.YELLOW + "Hubo un error")
			print (Back.BLACK + Fore.WHITE)
			client.close
			break

def write_messages():
	while True:
		message = f"{username}:	{input('>>> ')}"
		client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()

