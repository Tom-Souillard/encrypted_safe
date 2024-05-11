from cryptography.fernet import Fernet

class EncryptionKey:
    def __init__(self, key=None):
        """Initialise la clé de chiffrement. Génère une nouvelle clé si aucune n'est fournie."""
        self.key = key if key else Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        """Chiffre les données fournies à l'aide de la clé de chiffrement."""
        return self.cipher.encrypt(data)

    def decrypt_data(self, encrypted_data):
        """Déchiffre les données fournies à l'aide de la clé de chiffrement."""
        return self.cipher.decrypt(encrypted_data)
