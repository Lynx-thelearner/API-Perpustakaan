from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.config import settings

SUPABASE_POOLER = settings.SUPABASE_POOLER
SUPABASE_DIRECT = settings.SUPABASE_DIRECT

try:
    #Coba pooler dulu
    engine = create_engine(SUPABASE_POOLER, pool_pre_ping=True)
    with engine.connect() as conn:
        print("Connected to database using pooler")
except Exception as e1:
    print(f"Gagal pakai Pooler, coba direct link")
    try:
        engine = create_engine(SUPABASE_DIRECT, pool_pre_ping=True)
        with engine.connect() as conn:
            print("Connected to database using direct link")
    except Exception as e2:
        print("❌ Both Supabase connections failed.")
        print("Pooler error:", e1)
        print("Direct error:", e2)
        engine = create_engine(
            "sqlite:///./local_backup.db",
            connect_args={"check_same_thread": False}
        )

#buat session lokal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#buat base class untuk model
Base = declarative_base()

# Dependency buat dapetin session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()