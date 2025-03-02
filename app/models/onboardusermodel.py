from sqlalchemy import Column, Integer, String, Boolean, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class OnboardUser(Base):
    __tablename__ = "onboardusers"

    emp_id = Column(Integer, primary_key=True, index=True)  # Auto-incremented primary key
    emp_name = Column(String(50), nullable=False)  # Required, max length 50
    emp_role = Column(Text, nullable=False)  # Required
    position = Column(Text, nullable=False)  # Required
    notes = Column(Text, nullable=True)  # Optional
    created_on = Column(TIMESTAMP, default=datetime.utcnow)  # Auto-set timestamp
    is_deleted = Column(Boolean, default=False)  # Default is False
    email = Column(String(255), nullable=False, unique=True)  # Required and unique
    is_allowed = Column(Boolean, default=True)  # Default is True

