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

# Dateiname der verschlüsselten Textdatei
encrypted_file = r"Tag_4_Securety\secure_2.txt"

# Verschiebung für die Caesar-Verschlüsselung
shift = -5  # Du kannst die Anzahl der Positionen anpassen

try:
    with open(encrypted_file, "r") as file:
        ciphertext = file.read()
    decrypted_text = decrypt_caesar_cipher(ciphertext, shift)

    # Ausgabe des entschlüsselten Texts
    print("Entschlüsselter Text:")
    print(decrypted_text)
except FileNotFoundError:
    print(f"Die Datei '{encrypted_file}' wurde nicht gefunden.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {str(e)}")
