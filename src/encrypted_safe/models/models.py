from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from werkzeug.security import check_password_hash

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def check_password(self, password: str) -> bool:
        """Check hashed password against entered password."""
        return check_password_hash(self.hashed_password, password)
