# Important Pre-requisites
## Opening Files
To open and read files in Python, you can use the following code:
```python
with open("file_path", "r") as file:
    ciphertext = file.read()
```
This creates a variable named `ciphertext` that contains the content of the file.
Important!!!
The variable can only be used inside the `with` block.

## Working with Characters
To convert a character to Unicode in Python, use `ord(char)`, where `char` is a variable containing the character.
To convert Unicode back to a 'normal' character (reversing the previous process), use `chr(unicode)`.

## Opening Zip Files
Zip files compress multiple files into a single file to save space.
To open them in Python, use the following code:
```python
import zipfile
zip_file_path = 'your_zip_file.zip'  # Adjust the path to the zip file
password = 'your_password'  # Adjust the password
with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
    # Try to open the zip file with the given password
    zip_file.extractall(path='unzipped_folder', pwd=password.encode('utf-8'))
```
If you are not sure if the password is correct, you can extend the code like this:
```python
import zipfile
zip_file_path = 'your_zip_file.zip'  # Adjust the path to the zip file
password = 'your_password'  # Adjust the password
try:
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        # Try to open the zip file with the given password
        zip_file.extractall(pwd=password.encode('utf-8'))
        print(f'The zip file was successfully opened and extracted with the password "{password}".')
except Exception as e:
    print(f'An unknown error occurred: {str(e)}')
```
Important!!! The variable `password` must be a string. Otherwise, the `encode('utf-8')` function cannot be used.

## Python Server
To connect to a Python server, you can use the following code:
```python
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
```
By specifying the correct port and host, your program can successfully connect to the server.

To communicate with the server, you can use the following code:
```python
# Sending messages to the server
message = "Hello, Server!"
client_socket.sendall(message.encode('utf-8'))

# Receiving messages from the server
response = client_socket.recv(1024).decode('utf-8')
# The 1024 here stands for the number of bytes you want to receive at most
# Leave it at 1024 for now
```
Important! Don't forget to use `encode('utf-8')` when sending and `.decode('utf-8')` when receiving! Otherwise, you'll only get Klingon 😂.

When you're done with the communication, always close the connection:
```python
client_socket.close()
```


# Cybersecurity Challenge
## Task 1: Caesar Cipher
In the file `secure_2.txt`, there is an encrypted text. Try to decrypt the text. Write a program to automate this.

## Task 2: Caesar Cipher Brute Force
The file `secure_2.txt` contains a quote in the Caesar cipher. It is only known that the word `Digitalisierung` (which means "digitalization" in German) is in the text. Write a Python program and crack the text.

## Task 3: Encrypted Zip File
The zip file `task_3.zip` has been protected with a 4-digit PIN. Write a Python program to guess the PIN.

## Task 4: Encrypted Zip File with Password
Now it gets a bit more complicated! The zip file `task_4.zip` is now encrypted with a password. It might help to use the `password-list.txt`.

## Task 5: Connect to a Python Server
In the `server` folder, there is the Python program `server.py`. This program provides a simple server that accepts connections on IP: '127.0.0.1' and port: '12345'. Write a simple Python script to connect to the server.

## Task 6: Server with Password Protection
In the `server` folder, there is the Python program `server_password.py`. This server is now protected with a random PIN as a password.

Info! Only after the server sends the message `Enter the password:`, a password can be sent.
Extend your program from Task 5 and add a password cracker to it.

## Task 7: Server with Timeout
In the `server` folder, there is the Python program `server_pass_timeout.py`. This server works like the one from Task 6, but it waits for 5 seconds after each wrong password and only then allows input again.

Since this task is very difficult, the password can be read from the server file. But the goal is to guess the password without cheating.

Please note that the above translation is provided for your convenience, and you can use it as a reference for your tasks. If you have any specific questions or need further assistance with any of the tasks, feel free to ask. Good luck with your cybersecurity challenge!