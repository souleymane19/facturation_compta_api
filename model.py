from sqlalchemy import Boolean, Column, Integer, String, Table, ForeignKey
from pydantic import BaseModel
from sqlalchemy.orm import relationship

from config.database import Base

# Table de liaison pour la relation many-to-many
user_roles = Table(
    'user_roles', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
)


class User(BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    hashed_password = Column(String)
    is_active = Column(Boolean)
    roles = relationship("Role", secondary=user_roles, back_populates="users")


class Role(BaseModel):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user = relationship("User", secondary=user_roles, back_populates="Roles")

