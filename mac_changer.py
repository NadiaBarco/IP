
import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:34:44:11:66:22", shell=True)
"""
lo que hace la tercera linea de codifo es cambiar nuestra direccion mac 
y lo podemos verificar con el comando ifconfig en la terminal
"""
subprocess.call("ifconfig eth0 up", shell=True)