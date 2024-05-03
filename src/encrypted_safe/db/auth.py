# from sqlalchemy.orm import Session
from src.encrypted_safe.db.database import SessionLocal
from src.encrypted_safe.models.models import User
from src.encrypted_safe.utils.logging_config import logger

def login(username: str, password: str) -> bool:
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
    if user and user.check_password(password):  # Supposons que vous avez une méthode pour vérifier le mot de passe
        logger.info(f"User {username} - Action: Logged in")
        return True
    logger.info(f"Failed login attempt for {username}")
    return False

def logout(username: str):
    # Dans un contexte réel, vous pourriez gérer la session ici
    logger.info(f"User {username} - Action: Logged out")
