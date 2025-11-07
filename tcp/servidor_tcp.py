# servidor_tcp.py
import socket
import datetime

# Configuración del servidor
HOST = '127.0.0.1'   # Dirección local
PORT = 5000          # Puerto del servidor

# Crear socket TCP (orientado a conexión)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a la dirección y puerto
server_socket.bind((HOST, PORT))

# Poner el servidor en modo escucha (máx. 5 conexiones en espera)
server_socket.listen(5)
print(f"Servidor TCP escuchando en {HOST}:{PORT}...")

# Contador de conexiones
conexion_count = 0

while True:
    # Esperar una conexión
    conn, addr = server_socket.accept()
    conexion_count += 1
    print(f"Cliente conectado desde {addr}")

    # Enviar mensaje al cliente
    hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje = f"Hola cliente {conexion_count}! La hora actual es {hora_actual}"
    conn.sendall(mensaje.encode())

    # Cerrar conexión con este cliente
    conn.close()
    print(f"Conexión con {addr} finalizada.\n")
