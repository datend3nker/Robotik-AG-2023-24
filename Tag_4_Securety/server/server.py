import socket

# Server-Konfiguration
host = '127.0.0.1'  # Lokale IP-Adresse
port = 12345       # Portnummer

# Socket erstellen und binden
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

# Auf Verbindungen warten
server_socket.listen(1)
print(f"Server lauscht auf {host}:{port}")

# Verbindung akzeptieren
client_socket, client_address = server_socket.accept()
print(f"Verbindung von {client_address} hergestellt")

# Nachrichten empfangen und ausgeben
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Empfangene Nachricht: {data.decode('utf-8')}")

# Verbindung schließen
client_socket.close()
