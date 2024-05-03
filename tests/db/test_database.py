from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from src.encrypted_safe.models.models import Base, User
from src.encrypted_safe.crud.crud import create_user, get_user_by_username

engine = create_engine('sqlite:///:memory:')
db = scoped_session(sessionmaker(bind=engine))

Base.metadata.create_all(engine)

def test_create_user():
    username = "testuser"
    email = "test@example.com"
    hashed_password = "securehashedpassword"
    user = create_user(db, username, email, hashed_password)
    assert user.username == username

def test_get_user_by_username():
    username = "testuser"
    user = get_user_by_username(db, username)
    assert user is not None