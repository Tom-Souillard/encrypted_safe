import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DATABASE_URI = 'sqlite:///prod.db'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///test.db'
