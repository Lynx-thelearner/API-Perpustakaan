#Import yang diperlukan
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Buat konfigurasi dasar env"""
    
    #Database settings
    SUPABASE_POOLER: str
    SUPABASE_DIRECT: str
    
    #JWT settings
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    #App settings
    app_name: str = "Sistem Peminjaman"
    app_version: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    debug: bool = True
    
    class Config:
        """Lokasi file .env dan encodingnya"""
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()