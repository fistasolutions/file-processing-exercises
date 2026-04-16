"""
Game Inventory -- Data Models
These models are CORRECT. Do not modify them.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    gold = Column(Integer, nullable=False, default=0)

    items = relationship("Item", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Player: {self.username} ({self.gold} gold, {len(self.items)} items)>"


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    value = Column(Integer, nullable=False, default=0)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)

    owner = relationship("Player", back_populates="items")

    def __repr__(self):
        return f"<Item: {self.name} (value={self.value}, owner={self.player_id})>"
