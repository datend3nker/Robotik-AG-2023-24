import base64


encrypted_password = "c2VjcmV0X3Bhc3N3b3Jk"

def decrypt_password(encrypted):
    decoded = base64.b64decode(encrypted).decode("utf-8")
    return decoded

if __name__ == "__main__":
    user_input = input("Geben Sie das Passwort ein: ")
    
    if user_input == decrypt_password(encrypted_password):
        print("Herzlichen Glückwunsch! Sie haben das richtige Passwort gefunden.")
    else:
        print("Falsches Passwort. Bitte versuchen Sie es erneut.")