import socket
import time

# Server-Konfiguration
host = '127.0.0.1'  # Lokale IP-Adresse
port = 12345       # Portnummer
password = "geheimes_passwort"
Timeout = 5

# Socket erstellen und binden
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

# Auf Verbindungen warten
server_socket.listen(1)
print(f"Server lauscht auf {host}:{port}")
client_socket, client_address = server_socket.accept()
print(f"Verbindung von {client_address} hergestellt")

while True:
    client_socket.sendall("Geben Sie das Passwort ein: ".encode('utf-8'))
    received_password = client_socket.recv(1024).decode('utf-8')
    if received_password == password:
        client_socket.sendall("Erfolgreich angemeldet!\n".encode('utf-8'))
        break
    else:
        client_socket.sendall("Falsches Passwort. 5s Timeout.\n".encode('utf-8'))
        time.sleep(Timeout)

# Verbindung schließen
client_socket.close()
