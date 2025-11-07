# cliente_udp.py
import socket

# Configuración del cliente
HOST = '127.0.0.1'  # IP del servidor
PORT = 6000         # Puerto del servidor

# Crear socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar mensaje al servidor
mensaje = "¿Qué hora es?"
client_socket.sendto(mensaje.encode(), (HOST, PORT))

# Esperar respuesta del servidor
data, server = client_socket.recvfrom(1024)
print("Respuesta del servidor:")
print(data.decode())

# Cerrar socket
client_socket.close()
