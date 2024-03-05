import socket

# Server-Konfiguration
host = '127.0.0.1'  # Lokale IP-Adresse des Servers
port = 12345       # Portnummer des Servers
try:
    # Socket erstellen und Verbindung zum Server herstellen
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    while True:
        # passwortaufforderung
        response = client_socket.recv(1024).decode('utf-8')
        password = input(response)

        # Passwort an den Server senden
        client_socket.sendall(password.encode('utf-8'))

        # Server-Antwort empfangen und ausgeben
        response = client_socket.recv(1024).decode('utf-8')
        print(response)
        if "Erfolgreich" in response:
            break
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {str(e)}")
finally:
    # Verbindung schließen
    client_socket.close()
