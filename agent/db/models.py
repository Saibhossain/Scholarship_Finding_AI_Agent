from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from agent.db.database import Base

class UserProfile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)

    name = Column(String)
    level = Column(String)
    gpa = Column(Float)
    field = Column(String)
    country_preference = Column(String)
    english_test = Column(String)


class Essay(Base):
    __tablename__ = "essays"

    id = Column(Integer, primary_key=True)
    session_id = Column(String)

    content = Column(Text)
    feedback = Column(Text)