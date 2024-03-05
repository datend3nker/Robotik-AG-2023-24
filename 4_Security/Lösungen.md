# Lösungen su den Securetyaufgaben
## Aufgabe 1
### Beispielcode
```python
def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text
```
### Lösungsweg
Der Text kann mithilfe eines Caesarchiffre mit einem Shift von 12 gelöst werden

## Aufgabe 2
### Beispielcode
```python
def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

encrypted_text = "Jx lngy btmq pjnsjs Gjwjnhm, ns ijr inj Inlnyfqnxnjwzsl sthm snhmy fsljptrrjs nxy. Wtgtyjw, Fuux zsi Xrfwyumtsjx jwqjnhmyjws zsxjwjs Fqqyfl. Bnw fqqj rF¼xxjs zsx fzk bjnywjnhmjsij AjwF¤sijwzsljs jnsxyjqqjs. Ijssthm nxy inj Ezpzsky ijw Inlnyfqnxnjwzsl nxy ljxunhpy rny F„slxyjs zsi Atwgjmfqyjs. Wnhmynl nxy: Nrrjw rjmw Wtgtyjw zsi ajwsjyeyj LjwF¤yj knsijs nmwjs Bjl fzhm ns zsxjwjs Fwgjnyxfqqyfl. Ajwxhmnjijsj Xyzinjs ejnljs: Jx pF¶ssjs ebfw anjqj, bjsnljw vzfqnknenjwyj Otgx bjlkfqqjs, ithm ifkF¼w sjzj, bjsnljw fsxywjsljsij YF¤ynlpjnyjs ljxhmfkkjs bjwijs."

# Bruteforce durchführen, indem der Shift-Wert schrittweise erhöht wird
for shift in range(1, 26):
    decrypted_text = decrypt_caesar_cipher(encrypted_text, shift)
    
    # Überprüfen, ob das Wort "Digitalisierung" im entschlüsselten Text vorkommt
    if "Digitalisierung" in decrypted_text:
        print(f"Entschlüsselter Text mit Shift {shift}:")
        print(decrypted_text)
        break
```
### Lösungsweg
Shift erhöhen, bis das word 'Digitalisierung' im text vorkommt. der Shift ist 5

## Aufgabe 3
### Beispielcode
```python
import zipfile

passcode = 0
while True:
    try:
        with zipfile.ZipFile(r'Tag_4_Securety\aufgabe_3.zip', 'r') as zip_file:
            # Versuche, die Zip-Datei mit dem gegebenen Passwort zu öffnen
            zip_file.extractall(pwd=str(passcode).encode('utf-8'))
    except Exception as e:
        print(passcode, e)
        passcode += 1
        continue
    print(f'Die Zip-Datei wurde erfolgreich mit dem Passwort "{passcode}" geöffnet und entpackt.')
    break
```
### Lösungsweg
Das Password ist: 3965

## Aufgabe4
### Beispielcode
```python
with open(r'Tag_4_Securety\password-list.txt', 'r') as password_file:
    password_list = password_file.read().splitlines()

for password in password_list:
    try:
        with zipfile.ZipFile(r'Tag_4_Securety\aufgabe_4.zip', 'r') as zip_file:
            zip_file.extractall(pwd=password.encode('utf-8'))
        print(f'Passwort gefunden: {password}')
        break
    except Exception:
        continue
else:
    print('Das Passwort konnte nicht gefunden werden.')
```
### Lösungsweg
Das Password ist: cxfcnkbdxbr

## Aufgabe 5
```python
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
```

## Aufgabe 6
```python
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
```

## Aufgabe 7
Noch keine Lösung 
```python
```