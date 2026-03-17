from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..database import Base
from sqlalchemy.orm import relationship



class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    event_time = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


    bookings = relationship("Booking", back_populates="event")

