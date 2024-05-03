import pytest
from src.encrypted_safe.core.encryption import MyCrypt

@pytest.fixture
def crypt_instance():
    return MyCrypt()

def test_encrypt(crypt_instance):
    # Test encryption with a simple password
    password = "password123"
    encrypted_password = crypt_instance.encrypt(password)
    assert password != encrypted_password  # Check if password is encrypted

    # Test encryption with special characters
    special_chars_password = "!@#$%^&*()"
    encrypted_special_chars_password = crypt_instance.encrypt(special_chars_password)
    assert special_chars_password != encrypted_special_chars_password  # Check if special characters are encrypted

    # Test encryption with Unicode characters
    unicode_password = "你好，世界！"
    encrypted_unicode_password = crypt_instance.encrypt(unicode_password)
    assert unicode_password != encrypted_unicode_password  # Check if Unicode characters are encrypted

    # Test encryption with long password
    long_password = "a" * 1000
    encrypted_long_password = crypt_instance.encrypt(long_password)
    assert long_password != encrypted_long_password  # Check if long password is encrypted