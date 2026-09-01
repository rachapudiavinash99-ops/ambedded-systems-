from sqlalchemy import Column, Integer, String, ForeignKey
from .user import Base

class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    topic_id = Column(Integer, ForeignKey('topics.id'))
