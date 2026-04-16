"""
Task Manager -- Data Models
These models are CORRECT. Do not modify them.
"""

from datetime import datetime, date

from sqlalchemy import Column, Integer, String, Date, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    status = Column(String(20), nullable=False, default="pending")  # pending, in_progress, done
    priority = Column(Integer, nullable=False, default=3)  # 1=highest, 5=lowest
    due_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task #{self.id}: {self.title} [{self.status}] P{self.priority}>"
