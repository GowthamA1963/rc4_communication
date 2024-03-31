# Import necessary modules
import socket  # Module for socket programming
from Crypto.Cipher import ARC4  # Module for encryption using ARC4 cipher

# Function to handle communication with a client
def handle_client(client_socket, client_address, key):
    # Create an RC4 cipher object with the shared key
    cipher = ARC4.new(key)
    
    # Receive data from the client
    while True:
        # Receive encrypted data from the client
        encrypted_data = client_socket.recv(1024)
        # If no data is received, break out of the loop
        if not encrypted_data:
            break
        # Decrypt the received encrypted data using the RC4 cipher
        decrypted_data = cipher.decrypt(encrypted_data)
        
        # Print both encrypted and decrypted messages
        print(f"Received encrypted message from {client_address}: {encrypted_data}")
        print(f"Decrypted message: {decrypted_data.decode()}")
    
    # Close the client socket
    client_socket.close()

# Main function to set up the server and handle incoming connections
def main():
    # Server configuration
    server_host = 'localhost'  # Server hostname or IP address
    server_port = 8888          # Server port number
    key = b'shared_key'         # Shared key for encryption and decryption

    # Create a new socket object for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the server socket to the specified address and port
    server_socket.bind((server_host, server_port))
    # Set the server socket to listening mode, allowing it to accept incoming connections
    server_socket.listen(5)
    # Print a message indicating that the server is now listening
    print(f"Server listening on {server_host}:{server_port}")

    # Main loop to continuously accept incoming connections and handle them
    while True:
        # Accept a new connection from a client, returning a new socket object and client address
        client_socket, client_address = server_socket.accept()
        # Print a message indicating that a connection has been accepted from a client
        print(f"Accepted connection from {client_address}")
        # Call the handle_client function to handle communication with the client
        handle_client(client_socket, client_address, key)

# Check if the script is being run directly
if __name__ == "__main__":
    # If so, call the main function to start the server
    main()
