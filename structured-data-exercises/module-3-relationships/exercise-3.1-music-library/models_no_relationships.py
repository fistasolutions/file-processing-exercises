"""
Music Library -- Data Models (NO relationships defined)
Foreign keys are in place, but relationship() calls are missing.
Your task: add relationship() with back_populates to all three models.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    country = Column(String(100))
    formed_year = Column(Integer)

    # TODO: Add relationship to albums here
    # Should be one-to-many with cascade="all, delete-orphan"

    def __repr__(self):
        return f"<Artist: {self.name} ({self.country}, {self.formed_year})>"


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    release_year = Column(Integer, nullable=False)
    artist_id = Column(Integer, ForeignKey("artists.id"), nullable=False)

    # TODO: Add relationship back to artist here
    # TODO: Add relationship to tracks here (one-to-many with cascade)

    def __repr__(self):
        return f"<Album: {self.title} ({self.release_year})>"


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    duration_seconds = Column(Integer, nullable=False)
    track_number = Column(Integer, nullable=False)
    album_id = Column(Integer, ForeignKey("albums.id"), nullable=False)

    # TODO: Add relationship back to album here

    def __repr__(self):
        return f"<Track #{self.track_number}: {self.title} ({self.duration_seconds}s)>"
