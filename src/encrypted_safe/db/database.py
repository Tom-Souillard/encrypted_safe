# src/encrypted_safe/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Chemin vers le fichier de la base de données SQLite
DATABASE_URL = "sqlite:///../../../data/test_database.db"

# Création du moteur de base de données
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

# Création d'une fabrique de sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base déclarative pour les modèles
Base = declarative_base()

def init_db():
    # Création de toutes les tables définies
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()