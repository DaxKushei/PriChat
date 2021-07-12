#!/usr/bin/env python
import os
import socket
import threading
from colorama import init
from colorama import Fore,init
from colorama import Back,init

os.system('clear')
print (Back.GREEN + Fore.WHITE + "PriChat v1.2")
print (Back.BLACK + Fore.WHITE)
print ("")
print ("[1]	Iniciar server")
print ("[2]	Unirme a un server")
print ("[99]	Salir")
option = input(">>> ")
if option=="1":
	os.system('clear')
	os.system('python server_prichat.py')
elif option=="2":
	os.system('clear')
	os.system('python client_prichat.py')
elif option=="99":
	os.system('clear')
	exit()
else:
	print ("Opcion Invalida")

