"""
Configuration management for the test framework.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration class."""
    
    BASE_URL = os.getenv("BASE_URL", "https://demo.ecommerce.local")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.demo.ecommerce.local")
    TIMEOUT = int(os.getenv("TIMEOUT", "5"))
    VERIFY_SSL = os.getenv("VERIFY_SSL", "true").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"


class DevelopmentConfig(Config):
    """Development environment configuration."""
    
    DEBUG = True
    HEADLESS = False


class StagingConfig(Config):
    """Staging environment configuration."""
    
    DEBUG = False
    TIMEOUT = 10


class ProductionConfig(Config):
    """Production environment configuration."""
    
    DEBUG = False
    VERIFY_SSL = True
    TIMEOUT = 15


def get_config(env: str = "dev") -> Config:
    """Get configuration for the specified environment."""
    configs = {
        "dev": DevelopmentConfig,
        "staging": StagingConfig,
        "prod": ProductionConfig,
    }
    return configs.get(env, DevelopmentConfig)()
