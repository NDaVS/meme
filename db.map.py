from sqlalchemy import  Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MediaIDs(Base):
    __tableName__ = 'Media ids'
    id = Column(Integer, primary_key=True)
    file_id = Column(String(255))
    file_name = Column(String(255))