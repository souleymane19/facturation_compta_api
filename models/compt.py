from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Compte(Base):
    __tablename__ = 'comptes'

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255))
    numero = Column(String(255))
    solde = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    users = relationship('users', back_populates='comptes')