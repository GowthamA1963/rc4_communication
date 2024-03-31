# Import necessary modules
import socket  # Module for socket programming
from Crypto.Cipher import ARC4  # Module for encryption using ARC4 cipher

# Main function for the client
def main():
    # Server configuration
    server_host = 'localhost'  # Server hostname or IP address
    server_port = 8888          # Server port number
    key = b'shared_key'         # Shared key for encryption and decryption

    # Create a new socket object for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Attempt to connect to the server
        client_socket.connect((server_host, server_port))
        # If connection is successful, print a message indicating successful connection
        print(f"Connected to server at {server_host}:{server_port}")
    except ConnectionRefusedError:
        # If connection is refused, print an error message and return from the function
        print(f"Error: Connection refused to {server_host}:{server_port}")
        return

    # Create an RC4 cipher object with the shared key
    cipher = ARC4.new(key)

    # Loop to continuously send messages to the server
    while True:
        try:
            # Prompt the user to enter a message
            message = input("Enter message: ")
            # Check if the user wants to quit
            if message.lower() == 'quit':
                break
            # Encrypt the message using the RC4 cipher
            encrypted_message = cipher.encrypt(message.encode())
            # Send the encrypted message to the server
            client_socket.sendall(encrypted_message)
        except KeyboardInterrupt:
            # If the user interrupts the program (e.g., with Ctrl+C), break out of the loop
            break
        except Exception as e:
            # If an error occurs, print an error message and break out of the loop
            print(f"Error: {e}")
            break

    # Close the client socket
    client_socket.close()

# Check if the script is being run directly
if __name__ == "__main__":
    # If so, call the main function to start the client
    main()
