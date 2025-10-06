from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Sqlite URL buat SQLalchemy
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:OAiIEV6GVmFMdR31@db.saustawcyfsykibsysow.supabase.co:5432/postgres"

#buat engine SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

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