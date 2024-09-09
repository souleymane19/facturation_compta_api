from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Paiement(Base):
    __tablename__ = 'paiements'

    id = Column(Integer, primary_key=True, index=True)
    montant = Column(Integer)
    datePaiement = Column(Date)
    moyenPaiement = Column(String(255))
    client_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship('cleint', back_populates='paiements')