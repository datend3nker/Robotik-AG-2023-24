import zipfile

# passcode = 0
# while True:
#     try:
#         with zipfile.ZipFile(r'Tag_4_Securety\aufgabe_3.zip', 'r') as zip_file:
#             # Versuche, die Zip-Datei mit dem gegebenen Passwort zu öffnen
#             zip_file.extractall(pwd=str(passcode).encode('utf-8'))
#     except Exception:
#         passcode += 1
#         continue
#     print(f'Die Zip-Datei wurde erfolgreich mit dem Passwort "{passcode}" geöffnet und entpackt.')
#     break


with open(r'Tag_4_Securety\password-list.txt', 'r') as password_file:
    password_list = password_file.read().splitlines()

pf = open(r'Tag_4_Securety\password-list.txt', 'r')
pl = pf.read().splitlines()

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
