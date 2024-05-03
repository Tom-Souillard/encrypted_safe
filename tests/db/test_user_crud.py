import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.encrypted_safe.models.models import Base, User
from src.encrypted_safe.db.user_crud import create_user, update_user, delete_user

# Configuration de la base de données de test
engine = create_engine('sqlite:///:memory:')
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db_session():
    db = TestingSessionLocal()
    yield db
    db.rollback()

def test_create_user(db_session):
    user = create_user(db_session, username="testuser", email="test@example.com", password="secure123")
    assert user.username == "testuser"
    assert user.email == "test@example.com"

def test_update_user_password(db_session):
    user = create_user(db_session, username="testuser", email="test@example.com", password="secure123")
    updated_user = update_user(db_session, user.id, "newsecure123")
    assert updated_user is not None
    assert updated_user.hashed_password != user.hashed_password  # assuming hash changes

def test_delete_user(db_session):
    user = create_user(db_session, username="testuser", email="test@example.com", password="secure123")
    delete_user(db_session, user.id)
    deleted_user = db_session.query(User).filter(User.id == user.id).first()
    assert deleted_user is None
