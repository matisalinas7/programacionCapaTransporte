# servidor_udp.py
import socket
import datetime

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 6000

# Crear socket UDP (sin conexión)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlazar dirección y puerto
server_socket.bind((HOST, PORT))
print(f"Servidor UDP escuchando en {HOST}:{PORT}...\n")

while True:
    # Esperar un mensaje (datagrama) del cliente
    data, addr = server_socket.recvfrom(1024)
    print(f"Mensaje recibido de {addr}: {data.decode()}")

    # Responder al cliente
    hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    respuesta = f"Hola desde UDP! Hora actual: {hora_actual}"
    server_socket.sendto(respuesta.encode(), addr)
