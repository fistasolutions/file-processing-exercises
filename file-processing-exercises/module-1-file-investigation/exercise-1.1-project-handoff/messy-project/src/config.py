"""Configuration management for the data pipeline."""

import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv("SECRET_KEY", "FAKE-secret-key-for-exercise")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///dev.db")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10 MB
    ALLOWED_EXTENSIONS = {".csv", ".json", ".txt", ".xlsx"}

class DevConfig(Config):
    """Development configuration."""
    DEBUG = True
    DATABASE_URL = "sqlite:///dev.db"

class ProdConfig(Config):
    """Production configuration."""
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")  # Must be set in production

CONFIGS = {
    "dev": DevConfig,
    "prod": ProdConfig,
}

def get_config(env=None):
    env = env or os.getenv("APP_ENV", "dev")
    return CONFIGS.get(env, DevConfig)
