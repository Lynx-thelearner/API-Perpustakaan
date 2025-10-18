#Import yang diperlukan
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Buat konfigurasi dasar env"""
    
    #Database settings
    SUPABASE_POOLER: str = "postgresql+asyncpg://user:password@localhost:5432/mydatabase"
    SUPABASE_DIRECT: str = "postgresql+asyncpg://user:password@localhost:5432/mydatabase"
    
    #JWT settings
    SECRET_KEY: str = "BEHRAHASIABANGET12345"
    ALGORITHM: str = "HS256"
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

if not settings.SUPABASE_POOLER:
    print("⚠️  [CONFIG WARNING] SUPABASE_POOLER belum di-set di .env.")
if not settings.SECRET_KEY or settings.SECRET_KEY == "BEHRAHASIABANGET12345":
    print("⚠️  [CONFIG WARNING] SECRET_KEY masih default, ganti di .env untuk production!")