from sqlalchemy import Column, Integer, String, Date, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

from enumeration.TypeFacturation import TypeFacturation

class Facture(Base):
    __tablename__ = 'facturation'

    id = Column(Integer, primary_key=True, index=True)
    numeroFacture = Column(String(255), unique=True, index=True)
    type = Column(Enum(TypeFacturation), nullable=False)  # Assurez-vous d'ajouter nullable=False si ce champ est requis
    dateEmission = Column(Date)
    dateEcheance = Column(Date)
    montantTotal = Column(Integer)
    statut = Column(String(255))  # Ex: payée, impayée, annulée
    note = Column(Text, nullable=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    client = relationship('Client', back_populates='factures')
    ligne_items = relationship('FacturationLigneItem', back_populates='facture')
    users = relationship("User", back_populates='facture')


