from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class LigneItem(Base):
    __tablename__ = 'LigneItem'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255))
    quantite = Column(Integer)
    prixUnitaire = Column(Integer)
    montantTotal = Column(Integer)

    item_id = Column(Integer, ForeignKey('items.id'))

    item = relationship('Items', back_populates='ligne_items')
