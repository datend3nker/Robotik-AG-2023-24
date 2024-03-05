# Wichtige Vorkenntnisse
## Öffnen von Dateien
Um in Python Dateien zu öffnen und lesen wird folgender code verwendet:
```python
with open("pfad zur Datei", "r") as file:
    ciphertext = file.read()
```
Dies erstellt eine Variable namens `ciphertext` welche den Inhalt der Datei beinhaltet.
Wichtig!!!
die Variable ist nur im Block des `with` zu benutzen.
## Arbeiten mit Zeichen
Um ein Zeichen in in Python zu Unicode umzuwandeln, benutzen wir die `ord(char)` wobei char eine Variable ist die das Zeichen beinhaltet.
Um Unicode zu einem 'normalen' Zeichen umzuwandeln (den vorigen Prozess umkehren) benutzen wir `chr(unicode)`
## Öffnen von Zip-Dateien
Zip-dateien sind Ordner zu einer einzigen Datei zusammengefasst, um Speicherplatz zu sparen.
Um diese in Python zu öffnen wird folgender Code benutzt:
```python
import zipfile
zip_file_path = 'deine_zip_datei.zip'  # Passe den Pfad zur Zip-Datei an
password = 'dein_passwort'  # Passe das Passwort an
with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
    # Versuche, die Zip-Datei mit dem gegebenen Passwort zu öffnen
    zip_file.extractall(path='entpackter_ordner', pwd=password.encode('utf-8'))
```
Falls man sich nicht sicher ist, ob das Password richtig ist, kann der Code so erweitert werden:
```python
import zipfile
zip_file_path = 'deine_zip_datei.zip'  # Passe den Pfad zur Zip-Datei an
password = 'dein_passwort'  # Passe das Passwort an
try:
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        # Versuche, die Zip-Datei mit dem gegebenen Passwort zu öffnen
        zip_file.extractall(pwd=password.encode('utf-8'))
        print(f'Die Zip-Datei wurde erfolgreich mit dem Passwort "{password}" geöffnet und entpackt.')
except Exception as e:
    print(f'Ein unbekannter Fehler ist aufgetreten: {str(e)}')
```
Wichtig!!! Die Pariable `password` muss ein Sting sein. Ansonsten kann die Funktion `encode('utf-8')` nicht benutzt werden

## Python Server
Um mit einem Python Server sich zu verbinden benötigen wir folgenden Code:
```python
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
```
Unter Angabe des richtigen Ports und Hosts verbindet sich so unser Programm erfolgreich mit dem Server.

Um nun mit dem Server kommunizieren zu können können wir folgenden code benutzten:
```python
# Nachrichten an den Server zu schicken
message = "Hallo, Server!"
client_socket.sendall(message.encode('utf-8'))

# Um Nachrichten vom Server zu empfangen.
response = client_socket.recv(1024).decode('utf-8')
# die 1024 steht hier für die Anzahl an Bytes die ihr maximal empfangen wollt
# Belasst es Erstmal bei 1024
```
Wichtig! Vergesse beim Senden das `encode('utf-8')` und beim Empfangen das `.decode('utf-8')` nicht! Sonst bekommt ihr nur Klingonisch 😂.

Wenn ihr Fertig mit der Kommunikation seid, immer die Verbindung schließen:
```python
client_socket.close()
```


# Aufgabe zur Cybersecurity
## Aufgabe 1: Caesar Chiffre
In der Datei `secure_2.txt`befindet sich ein verschlüsselter Text. Versuche den Text zu entschlüsseln.
Schreibe dazu ein Programm um das ganze zu automatisieren

## Aufgabe 2: Caesar Chiffre bruteforce
Die Datei `secure_2.txt` beinhaltet ein Zitat in der Caesar Chiffre.
Es ist leider nur bekannt, dass sich das Wort `Digitalisierung` im Text befindet.
Schreibe ein Python Programm und knacke den Text.

## Aufgabe 3: Verschlüsselte Zip-datei
Die Zip-datei `aufgabe_3.zip` wurde mit einer 4 stelligen Pin geschützt.
Schreibe ein Pythonprogram, um die Pin zu erraten.

## Aufgabe 3: Verschlüsselte Zip-datei
Nun wird es ein bisschen Komplizierter! Die Zip-Datei `aufgabe_4.zip` ist jetzt mit einem Passwort verschlüsselt.
Es könnte helfen die `password-list.txt` zu benutzen

## Aufgabe 4: Mit einem Python-Server verbinden
Im Ordner `server` befindet sich das Pythonprogram `server.py`. Diesen Programm stellt einen einfachen Server zur Verfügung, der mit der IP: '127.0.0.1' auf dem Port: '12345' Verbindungen akzeptiert.

Schreibe ein einfaches Pythonskript, um dich mit dem Server zu verbinden.

## Aufgabe 5: Server mit Passwortschutz
Im Ordner `server` befindet sich das Pythonprogram `server_password.py`. Dieser server ist nun mit einem zufälligen Pin als Passwort geschützt.

Info! Erst nachdem der Server die Nachricht `Geben Sie das Passwort ein: ` geschickt hat darf ein Password gesendet werden.

Erweiter hierzu dein Programm aus Aufgabe 4 und erweitere es um einen Passwortcracker

## Aufgabe 6: Server mit Timeout
Im Ordner `server` befindet sich das Pythonprogram `server_pass_timeout.py`. Dieser Server Funktioniert wie der aus Aufgabe 5, nur dass er nach jedem falschen Passwort 5 Sekunden wartet und erst dann wieder eine Eingabe erlaubt.

Da diese Aufgabe sehr schwer ist, kann das Password aus der Serverdatei ausgelesen werden. Aber ziel ist es das Passwort auch ohne schummeln zu erraten.
