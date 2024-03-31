import socket
from Crypto.Cipher import ARC4

def handle_client(client_socket, client_address, key):
    # Create an RC4 cipher object with the shared key
    cipher = ARC4.new(key)
    
    # Receive data from the client
    while True:
        encrypted_data = client_socket.recv(1024)
        if not encrypted_data:
            break
        decrypted_data = cipher.decrypt(encrypted_data)
        
        # Print both encrypted and decrypted messages
        print(f"Received encrypted message from {client_address}: {encrypted_data}")
        print(f"Decrypted message: {decrypted_data.decode()}")
    
    client_socket.close()

def main():
    server_host = 'localhost'
    server_port = 8888
    key = b'shared_key'

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print(f"Server listening on {server_host}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket, client_address, key)

if __name__ == "__main__":
    main()

