"""
Blog Platform -- Models with Relationships
WARNING: This file contains 5 relationship bugs. Do NOT use in production.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    bio = Column(Text)

    # BUG #1: back_populates="writers" but Post.author has back_populates="author"
    # These must match: Author.posts back_populates="author" <-> Post.author back_populates="posts"
    posts = relationship("Post", back_populates="writers", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author: {self.name}>"


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=False)
    published_at = Column(DateTime, default=datetime.utcnow)
    # BUG #4: ForeignKey references 'author.id' but table name is 'authors' (plural)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)

    author = relationship("Author", back_populates="posts")
    # BUG #2: cascade="all" is missing "delete-orphan"
    # Without delete-orphan, comments survive even when their parent post is deleted
    comments = relationship("Comment", back_populates="post", cascade="all")

    def __repr__(self):
        return f"<Post: {self.title}>"


class Comment(Base):
    # BUG #5: missing __tablename__ -- SQLAlchemy will use "comment" by default
    # but ForeignKey references expect "comments" (plural, conventional)

    id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    commenter_name = Column(String(100), nullable=False)
    posted_at = Column(DateTime, default=datetime.utcnow)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

    # BUG #3: references "Article" instead of "Post"
    post = relationship("Article", back_populates="comments")

    def __repr__(self):
        return f"<Comment by {self.commenter_name}>"
