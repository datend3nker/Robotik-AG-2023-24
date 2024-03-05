import socket

# Server-Konfiguration
host = '127.0.0.1'  # Lokale IP-Adresse
port = 12345       # Portnummer

# Nachricht an den Server senden
message = "Hallo, Server!"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
client_socket.sendall(message.encode('utf-8'))
client_socket.close()
