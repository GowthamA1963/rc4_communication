import socket
from rc4 import RC4  # Importing the RC4 class from a custom module

def main():
    host = "127.0.0.1"  # Server IP address
    port = 12345  # Server port number

    # Creating a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connecting to the server
    client_socket.connect((host, port))

    # Defining the encryption key
    key = b"SecretKey"
    rc4_key = RC4(key)  # Creating an instance of the RC4 class with the key

    # Main loop for sending and receiving messages
    while True:
        # Getting user input for the message to send
        message = input("Enter message: ")
        
        # Encrypting the message using RC4
        encrypted_message = rc4_key.encrypt(message.encode('utf-8'))
        
        # Printing the original and encrypted messages
        print("Original message:", message)
        print("Encrypted message:", encrypted_message)
        
        # Sending the encrypted message to the server
        client_socket.send(encrypted_message)

        # Receiving the response from the server
        response = client_socket.recv(4096)
        
        # Decrypting the response using RC4
        decrypted_response = rc4_key.decrypt(response)
        
        # Converting decrypted response to hexadecimal format for better readability
        decrypted_hex_response = " ".join([format(byte, "02x") for byte in decrypted_response])
        
        # Printing the decrypted response
        print("Decrypted response:", decrypted_hex_response.upper())

if __name__ == "__main__":
    main()
