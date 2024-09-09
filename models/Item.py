from sqlalchemy import Column, Integer, String, Enum, Text, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

from enumeration.TypeItem import TypeItem
class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(TypeItem))
    nom = Column(String(255), index=True)
    prixUnitaire = Column(Integer)
    description = Column(Text, nullable=True)
    users_id = Column(Integer, ForeignKey('items.id'))
    ligne_items = relationship('FacturationLigneItem', back_populates='item')


