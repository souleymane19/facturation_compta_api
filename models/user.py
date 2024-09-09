from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship

from config.database import Base
from enumeration.TypeRole import TypeRole


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    roles = Column(Enum(TypeRole))  # Enum pour les rôles

    compte = relationship('Compte', back_populates='user')
    client = relationship('client', back_populates='user')
    facturation = relationship('Facturation', back_populates='user')
    paiement = relationship('Paiement', back_populates='user')
    items = relationship('Item', back_populates='user')
