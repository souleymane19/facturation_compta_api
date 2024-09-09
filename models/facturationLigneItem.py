from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class FacturationLigneItem(Base):
    __tablename__ = 'facturationLigneItem'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255))
    quantite = Column(Integer)
    prixUnitaire = Column(Integer)
    montantTotal = Column(Integer)

    facture_id = Column(Integer, ForeignKey('facturation.id'))

    facture = relationship('Facture', back_populates='ligne_items')
