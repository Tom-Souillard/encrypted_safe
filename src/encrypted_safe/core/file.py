import os
class File:
    def __init__(self, path):
        self.path = path
        self.encrypted = False
        self.metadata = self._get_metadata()

    def _get_metadata(self):
        """Retrieve and store metadata for the file."""
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"The file at {self.path} does not exist.")

        stats = os.stat(self.path)
        return {
            'size': stats.st_size,
            'modification_date': stats.st_mtime,
            'is_directory': os.path.isdir(self.path)
        }

    def encrypt(self, encryption_key):
        """Encrypt the file using the provided encryption key."""
        if self.metadata['is_directory']:
            raise ValueError("Encryption of directories is not supported.")

        if not self.encrypted:
            with open(self.path, 'rb') as file:
                file_data = file.read()
            encrypted_data = encryption_key.encrypt_data(file_data)
            with open(self.path, 'wb') as file:
                file.write(encrypted_data)
            self.encrypted = True
            print(f"File {self.path} has been encrypted.")

    def decrypt(self, encryption_key):
        """Decrypt the file using the provided encryption key."""
        if self.metadata['is_directory']:
            raise ValueError("Decryption of directories is not supported.")

        if self.encrypted:
            with open(self.path, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = encryption_key.decrypt_data(encrypted_data)
            with open(self.path, 'wb') as file:
                file.write(decrypted_data)
            self.encrypted = False
            print(f"File {self.path} has been decrypted.")
