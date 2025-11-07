# cliente_tcp.py
import socket

# Configuración del cliente
HOST = '127.0.0.1'   # Mismo host que el servidor
PORT = 5000          # Mismo puerto

# Crear socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor
client_socket.connect((HOST, PORT))

# Esperar mensaje del servidor
mensaje = client_socket.recv(1024).decode()
print("Mensaje recibido del servidor:")
print(mensaje)

# Cerrar conexión
client_socket.close()
