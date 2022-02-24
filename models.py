from sqlalchemy import Column, Numeric, Integer, String
from database import Base


class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    request = Column(String)
    response = Column(String)
    status = Column(String)

