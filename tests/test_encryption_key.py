import pytest
from cryptography.fernet import Fernet
from encrypted_safe.core.encryption_key import EncryptionKey

def test_encryption_key_initialization():
    """Teste si la clé de chiffrement est correctement initialisée."""
    key = EncryptionKey()
    assert key.key is not None
    assert isinstance(key.cipher, Fernet)

def test_encrypt_decrypt():
    """Teste les fonctions de chiffrement et de déchiffrement."""
    key = EncryptionKey()
    message = b"Secret message"
    encrypted_message = key.encrypt_data(message)
    assert encrypted_message != message
    decrypted_message = key.decrypt_data(encrypted_message)
    assert decrypted_message == message
