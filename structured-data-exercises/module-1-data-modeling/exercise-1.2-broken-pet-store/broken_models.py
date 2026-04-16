"""
Pet Store Management System -- Models
WARNING: This file contains 6 bugs. Do NOT use in production.
"""

from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# BUG: ForeignKey is not imported above -- this will cause an error
# when Python tries to use ForeignKey in the Pet model.

Base = declarative_base()


class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150))  # BUG: missing unique=True
    phone = Column(String(20))
    address = Column(Text)

    pets = relationship("Pet", back_populates="owner")


class Pet(Base):
    __table__ = "pets"  # BUG: should be __tablename__, not __table__

    id = Column(Integer, primary_key=True)
    name = Column(Integer)  # BUG: should be String, not Integer
    species = Column(String(50), nullable=False)
    breed = Column(String(100))
    age = Column(Integer)
    weight = Column(Integer)
    owner_id = Column(Integer)  # BUG: missing ForeignKey("owners.id")

    owner = relationship("Owner", back_populates="pets")


class Vet(Base):
    __tablename__ = "vets"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    specialty = Column(String(100))
    license_number = Column(String(50))  # BUG: should have nullable=False
    clinic_name = Column(String(200))
    phone = Column(String(20))
