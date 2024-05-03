from sqlalchemy.orm import Session
from src.encrypted_safe.models.models import User
from src.encrypted_safe.utils.logging_config import logger
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(db: Session, username: str, email: str, password: str) -> User:
    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    logger.info(f"User {username} - Action: Created account")
    return user

def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

def update_user(db: Session, user_id: int, new_password: str) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if user and not check_password_hash(user.hashed_password, new_password):
        user.hashed_password = generate_password_hash(new_password)
        db.commit()
        return user
    return None

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
