import logging
from datetime import datetime
import os

def setup_logging():
    log_directory = os.path.join(os.path.dirname(__file__), '../../../logs')  # Ajustez le chemin selon la structure réelle
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)  # Crée le dossier s'il n'existe pas

    log_filename = datetime.now().strftime('EncryptedSafe_log_%Y-%m-%d.log')
    log_path = os.path.join(log_directory, log_filename)

    logger = logging.getLogger('EncryptedSafeLogger')
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

# Initialise le logger
logger = setup_logging()
