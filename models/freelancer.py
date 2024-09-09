from sqlalchemy import Column, Integer, String
from config.database import Base

class Freelancer(Base):
    __tablename__ = 'freelancers'

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255), index=True)
    adresse = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    numeroFiscal = Column(String(255))
    telephone = Column(String(255))
    siteWeb = Column(String(255), nullable=True)