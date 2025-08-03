
from urllib.parse import quote
import os
from dotenv import load_dotenv

load_dotenv()

ENV_MODE = os.environ.get("FLASK_ENV_MODE", "local")
def get_config():
    if ENV_MODE == "local":
        return LocalConfig
    elif ENV_MODE == "testing":
        return TestConfig
    elif ENV_MODE == "prod":
        return ProdConfig
    else:
        raise ValueError(f"Unknown FLASK_ENV_MODE: {ENV_MODE}")

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', os.urandom(32))  #  Replace with environment var in production

# Database config
    DB_NAME = os.environ.get('FLASK_DB_NAME', 'default_db_name')
    DB_USER = os.environ.get('FLASK_DB_USER', 'default_db_user')
    DB_PASSW = os.environ.get('FLASK_DB_PASS', 'default_db_password')
    DB_HOST = os.environ.get('FLASK_DB_HOST', 'localhost')
    DB_PORT = os.environ.get('FLASK_DB_PORT', '3306')

    DB_PASS_RAW = quote(DB_PASSW)

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS_RAW}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class LocalConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = "local-dev-testing" #replace

class TestConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = "testing-on-vps-123" #replace

class ProdConfig(BaseConfig):
    SECRET_KEY = os.urandom(32) # Make sure to replace this later



