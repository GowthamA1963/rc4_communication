class RC4:
    def __init__(self, key):
        """
        Initialize the RC4 instance with the given key.

        Args:
            key (bytes): The key used for encryption and decryption.
        """
        self.S = list(range(256))
        self.key = key
        self.i = 0
        self.j = 0
        self.initialize_state()

    def initialize_state(self):
        """
        Initialize the state array based on the key.
        """
        j = 0
        for i in range(256):
            j = (j + self.S[i] + self.key[i % len(self.key)]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

    def generate_keystream(self):
        """
        Generate a keystream byte by byte.

        Yields:
            int: A byte from the keystream.
        """
        i = self.i
        j = self.j
        while True:
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
            K = self.S[(self.S[i] + self.S[j]) % 256]
            yield K

    def encrypt(self, plaintext):
        """
        Encrypt the plaintext using RC4 algorithm.

        Args:
            plaintext (bytes): The plaintext to be encrypted.

        Returns:
            bytes: The encrypted ciphertext.
        """
        keystream = self.generate_keystream()
        encrypted = [char ^ next(keystream) for char in plaintext]
        return bytes(encrypted)

    def decrypt(self, ciphertext):
        """
        Decrypt the ciphertext using RC4 algorithm.

        Args:
            ciphertext (bytes): The ciphertext to be decrypted.

        Returns:
            bytes: The decrypted plaintext.
        """
        return self.encrypt(ciphertext)  # Decryption is the same as encryption in RC4
