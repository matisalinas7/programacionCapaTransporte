# 🧩 Práctico N°6 – Capa de Transporte

Este proyecto implementa aplicaciones **cliente-servidor** que se comunican mediante **sockets**, demostrando el funcionamiento de los **protocolos de transporte TCP y UDP** en la arquitectura TCP/IP.

---

## 🎯 Objetivo

Diseñar y programar un **cliente y servidor** que intercambien información utilizando:
- **TCP (orientado a la conexión)**: servicio confiable con control de flujo y verificación de entrega.  
- **UDP (no orientado a la conexión)**: servicio rápido sin necesidad de establecer conexión previa.

El propósito es observar las diferencias prácticas entre ambos mecanismos de transporte y comprender sus características principales dentro del modelo TCP/IP.

---

## ⚙️ Tecnologías utilizadas

- **Python 3.x**
- Módulo estándar `socket`
- Sistema operativo compatible con TCP/UDP (Windows, Linux o macOS)

---

## 📂 Estructura del proyecto

TP6_CapaTransporte/
│
├── tcp/
│ ├── servidor_tcp.py
│ └── cliente_tcp.py
│
├── udp/
│ ├── servidor_udp.py
│ └── cliente_udp.py
│
└── README.md

---

## 🚀 Ejecución

### 🔹 TCP (Orientado a conexión)

1. Abrir una terminal y ejecutar el servidor:
   python tcp/servidor_tcp.py
   
2. En otra terminal, ejecutar el cliente:
python tcp/cliente_tcp.py

📬 El cliente recibirá un mensaje con la hora actual y el número de conexión.

---

### 🔹 UDP (No orientado a conexión)

1. Abrir una terminal y ejecutar el servidor:
   python udp/servidor_udp.py

2. En otra terminal, ejecutar el cliente:
   python udp/cliente_udp.py

📬 El cliente enviará un mensaje (“¿Qué hora es?”) y recibirá la respuesta del servidor sin establecer conexión.
