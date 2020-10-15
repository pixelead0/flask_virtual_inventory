import os

DB_PSW = os.environ.get('DB_PSW', 'dev_psw')
DB_USER = os.environ.get('DB_USER', 'dev_user')
DB_NAME = os.environ.get('DB_NAME', 'dev_db')
DB_HOST = os.environ.get('DB_HOST', 'db')
postgres_local_base = f'postgresql://{DB_USER}:{DB_PSW}@{DB_HOST}/{DB_NAME}'


class Config:
    """Config flask"""
    SECRET_KEY = os.environ.get("SECRET_KEY", "placeholder-secret-key")
    SQLALCHEMY_DATABASE_URI = postgres_local_base


class DevelopmentConfig(Config):
    """Develoment Config """
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    """Testing Config """
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """Production Config """
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
