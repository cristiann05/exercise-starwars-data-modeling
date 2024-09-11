import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Tabla Usuario
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

    # Relación con la tabla Favorite
    favorites = relationship("Favorite", back_populates="user")

# Tabla Personaje
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))

    # Relación con la tabla Favorite
    favorites = relationship("Favorite", back_populates="character")

# Tabla Planeta
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))

    # Relación con la tabla Favorite
    favorites = relationship("Favorite", back_populates="planet")

# Tabla de Favoritos (relaciona Usuario con Planetas y Personajes)
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)

    # Relación con Usuario
    user = relationship("User", back_populates="favorites")

    # Relación con Personaje
    character = relationship("Character", back_populates="favorites")

    # Relación con Planeta
    planet = relationship("Planet", back_populates="favorites")

# Generar el diagrama a partir de los modelos
render_er(Base, 'diagram.png')
