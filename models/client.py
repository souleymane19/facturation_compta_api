from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255), index=True)
    adresse = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    telephone = Column(String(255))
    #Relation
    factures = relationship('Facture', back_populates='client')
    paiements = relationship('Paiement', back_populates='client')
