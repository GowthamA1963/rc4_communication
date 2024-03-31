import socket
from Crypto.Cipher import ARC4

def main():
    server_host = 'localhost'
    server_port = 8888
    key = b'shared_key'

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_host, server_port))
        print(f"Connected to server at {server_host}:{server_port}")
    except ConnectionRefusedError:
        print(f"Error: Connection refused to {server_host}:{server_port}")
        return

    # Create an RC4 cipher object with the shared key
    cipher = ARC4.new(key)

    # Loop to continuously send messages
    while True:
        try:
            message = input("Enter message: ")
            if message.lower() == 'quit':
                break
            encrypted_message = cipher.encrypt(message.encode())
            client_socket.sendall(encrypted_message)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

if __name__ == "__main__":
    main()

