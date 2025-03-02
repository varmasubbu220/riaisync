from sqlalchemy import Column, Integer, String, Boolean
from app.utils.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)  # Use user_id instead of id
    emp_id = Column(Integer, nullable=False)  # Foreign key reference to onboardusers
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    dob = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20), nullable=True)
    notes = Column(String, nullable=True)
    password = Column(String, nullable=False)
