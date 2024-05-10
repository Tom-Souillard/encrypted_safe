import pytest
from unittest.mock import MagicMock
import os
from encrypted_safe.core.file import File


@pytest.fixture
def mock_encryption_key():
    key = MagicMock()
    key.encrypt_data = MagicMock(return_value=b'encrypted_data')
    key.decrypt_data = MagicMock(return_value=b'Hello, world!')
    return key


@pytest.fixture
def test_file(tmp_path):
    test_file_path = tmp_path / "testfile.txt"
    test_file_path.write_text("Hello, world!")
    return str(test_file_path)


def test_file_metadata(test_file):
    file_instance = File(test_file)
    assert file_instance.metadata['size'] > 0
    assert file_instance.metadata['modification_date'] is not None
    assert not file_instance.metadata['is_directory']


def test_encrypt_decrypt_file(mock_encryption_key, test_file):
    file_instance = File(test_file)
    original_content = open(test_file, 'rb').read()

    # Test encryption
    file_instance.encrypt(mock_encryption_key)
    assert file_instance.encrypted
    encrypted_content = open(test_file, 'rb').read()
    assert encrypted_content == b'encrypted_data'

    # Reset file content for decryption test
    file_instance.encrypted = True

    # Test decryption
    file_instance.decrypt(mock_encryption_key)
    assert not file_instance.encrypted
    decrypted_content = open(test_file, 'rb').read()
    assert decrypted_content == b'Hello, world!'
