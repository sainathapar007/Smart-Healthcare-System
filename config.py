"""
Configuration settings for Smart Healthcare Management System.
Uses environment variables for sensitive data.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    DEBUG = False
    TESTING = False

    # Dataset Paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    TRAINING_DATA_PATH = os.path.join(DATA_DIR, "Training.csv")
    SYMPTOMS_DATA_PATH = os.path.join(DATA_DIR, "symtoms_df.csv")
    PRECAUTIONS_DATA_PATH = os.path.join(DATA_DIR, "precautions_df.csv")
    WORKOUT_DATA_PATH = os.path.join(DATA_DIR, "workout_df.csv")
    DESCRIPTION_DATA_PATH = os.path.join(DATA_DIR, "description.csv")
    MEDICATIONS_DATA_PATH = os.path.join(DATA_DIR, "medications.csv")
    DIET_DATA_PATH = os.path.join(DATA_DIR, "diets.csv")

    # Model Path
    MODEL_PATH = os.path.join(BASE_DIR, "models", "svc_model.pkl")

    # Logging
    LOG_LEVEL = "INFO"
    LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    LOG_LEVEL = "DEBUG"


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")  # Must be set in environment


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
