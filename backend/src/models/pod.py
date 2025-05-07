from sqlalchemy import Column, Integer, String, ARRAY
from models.user import Base

class Pod(Base):
    __tablename__ = "pods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    members = Column(ARRAY(Integer))  # Array of user IDs
