import socket
import random

# Server-Konfiguration
host = '127.0.0.1'  # Lokale IP-Adresse
port = 12345     # Portnummer
password = str(random.randint(0, 1000))

# Socket erstellen und binden
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

# Auf Verbindungen warten
server_socket.listen(1)
print(f"Server lauscht auf {host}:{port}")

# Verbindung akzeptieren
client_socket, client_address = server_socket.accept()
print(f"Verbindung von {client_address} hergestellt")

# Passwortprüfung
while True:
    client_socket.sendall("Geben Sie das Passwort ein: ".encode('utf-8'))
    received_password = client_socket.recv(1024).decode('utf-8')
    if received_password == password:
        client_socket.sendall("Erfolgreich angemeldet!\n".encode('utf-8'))
        break
    else:
        client_socket.sendall("Falsches Passwort! Bitte erneut versuchen\n".encode('utf-8'))

# Verbindung schließen
client_socket.close()
