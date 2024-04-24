import socket
from rc4 import RC4  # Importing the RC4 class from a custom module

def handle_client(client_socket, client_address, rc4_key):
    # Function to handle communication with a client
    print(f"Connection from {client_address}")

    while True:
        # Receiving data from the client
        data = client_socket.recv(4096)

        # Checking if the client has disconnected
        if not data:
            print(f"Client {client_address} disconnected.")
            break

        # Decrypting the received data using RC4
        decrypted_data = rc4_key.decrypt(data)
        
        # Converting decrypted data to hexadecimal format for better readability
        decrypted_hex_data = " ".join([format(byte, "02x") for byte in decrypted_data])

        # Printing the decrypted data
        print(f"Received from {client_address}: {decrypted_hex_data.upper()}")

        # Processing the decrypted message and generating a response
        response = input("Enter response: ")
        
        # Encrypting the response using RC4
        encrypted_response = rc4_key.encrypt(response.encode('utf-8'))
        
        # Sending the encrypted response back to the client
        client_socket.send(encrypted_response)

    # Closing the client socket when communication is finished
    client_socket.close()

def main():
    host = "127.0.0.1"  # Server IP address
    port = 12345  # Server port number

    # Creating a TCP socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Binding the socket to the specified host and port
    server_socket.bind((host, port))
    
    # Listening for incoming connections with a maximum backlog of 5
    server_socket.listen(5)

    # Printing a message indicating that the server is listening
    print(f"Server listening on {host}:{port}")

    # Defining the encryption key
    key = b"SecretKey"
    rc4_key = RC4(key)  # Creating an instance of the RC4 class with the key

    # Main loop for accepting and handling client connections
    while True:
        # Accepting a new client connection
        client_socket, client_address = server_socket.accept()
        
        # Handling communication with the client in a separate function
        handle_client(client_socket, client_address, rc4_key)

if __name__ == "__main__":
    main()
