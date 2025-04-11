from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv('DATABASE_URL')

Base = declarative_base()

class Inspection(Base):
    __tablename__ = 'inspections'
    
    id = Column(Integer, primary_key=True)
    boat_name = Column(String, nullable=False)
    boat_type = Column(String, nullable=False)
    boat_length = Column(Float, nullable=False)
    safety_devices_present = Column(String, nullable=False)
    notes = Column(String)
    inspection_status = Column(String, nullable=False)
    failure_reason = Column(String)

def get_engine():
    return create_engine(DATABASE_URL)

def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()