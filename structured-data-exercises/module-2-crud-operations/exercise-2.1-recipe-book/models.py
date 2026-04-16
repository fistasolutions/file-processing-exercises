"""
Recipe Book -- Data Models
These models are CORRECT. Do not modify them.
"""

from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    cuisine = Column(String(50), nullable=False)
    prep_time_minutes = Column(Integer, nullable=False)
    difficulty = Column(String(20), nullable=False)  # easy, medium, hard
    ingredients_count = Column(Integer, nullable=False)
    is_vegetarian = Column(Boolean, default=False)

    def __repr__(self):
        veg = " [V]" if self.is_vegetarian else ""
        return f"<Recipe: {self.title} ({self.cuisine}, {self.prep_time_minutes}min, {self.difficulty}){veg}>"


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"<Tag: {self.name}>"
