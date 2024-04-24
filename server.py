import socket
from rc4 import RC4

def handle_client(client_socket, client_address, rc4_key):
    print(f"Connection from {client_address}")
    while True:
        data = client_socket.recv(4096)
        if not data:
            print(f"Client {client_address} disconnected.")
            break
        decrypted_data = rc4_key.decrypt(data)
        decrypted_hex_data = " ".join([format(byte, "02x") for byte in decrypted_data])
        print(f"Received from {client_address}: {decrypted_hex_data.upper()}")
        response = input("Enter response: ")  # Process the decrypted message
        encrypted_response = rc4_key.encrypt(response.encode('utf-8'))
        client_socket.send(encrypted_response)
    client_socket.close()

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    key = b"SecretKey"
    rc4_key = RC4(key)

    while True:
        client_socket, client_address = server_socket.accept()
        handle_client(client_socket, client_address, rc4_key)

if __name__ == "__main__":
    main()
