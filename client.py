import socket
from rc4 import RC4

def main():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    key = b"SecretKey"
    rc4_key = RC4(key)

    while True:
        message = input("Enter message: ")
        encrypted_message = rc4_key.encrypt(message.encode('utf-8'))  # Encrypt the message
        print("Original message:", message)
        print("Encrypted message:", encrypted_message)
        client_socket.send(encrypted_message)  # Send the encrypted message

        response = client_socket.recv(4096)
        decrypted_response = rc4_key.decrypt(response)  # Decrypt the response
        print("Decrypted response:", decrypted_response.decode('utf-8'))

if __name__ == "__main__":
    main()
