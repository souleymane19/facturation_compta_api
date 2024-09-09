import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base de données SQLite
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost:3306/facturation_compta"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Déclaration de la base avec la version corrigée
Base = declarative_base()
