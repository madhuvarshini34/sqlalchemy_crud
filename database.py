# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL)

# Session configuration
Session = sessionmaker(bind=engine)

# Ensure that all the tables are created
def init_db():
    from models import Base
    Base.metadata.create_all(engine)

# Initialize a session
def get_session():
    return Session()
