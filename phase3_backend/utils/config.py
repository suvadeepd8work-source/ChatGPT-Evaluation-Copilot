from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables from root
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
env_path = os.path.join(root_dir, '.env')

class Settings(BaseSettings):
    PROJECT_NAME: str = "ChatGPT Evaluation Mode"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # LLM Providers
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    GROQ_API_KEY: Optional[str] = None
    
    # Search & Fact Checking
    SERPER_API_KEY: Optional[str] = None
    GOOGLE_SEARCH_API_KEY: Optional[str] = None
    GOOGLE_SEARCH_CX: Optional[str] = None
    
    # Database
    DATABASE_URL: str = "sqlite:///./storage/evaluation.db"
    
    # Connection Settings
    BACKEND_URL: str = "http://localhost:8000"
    FRONTEND_URL: str = "http://localhost:3000"
    ENVIRONMENT: str = "development"
    
    # Application Settings
    APP_ENV: str = "development"
    SECRET_KEY: str = "SECRET"
    PORT: int = 8000
    
    # Feature Flags
    ENABLE_SOURCE_AUDITOR: bool = True
    ENABLE_DEBIASING_UI: bool = True
    STAKE_DETECTION_THRESHOLD: float = 0.7

    model_config = SettingsConfigDict(env_file=env_path, case_sensitive=True, extra="ignore")

settings = Settings()
