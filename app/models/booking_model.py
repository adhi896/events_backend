from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from ..database import Base
from sqlalchemy.orm import relationship



class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    event = relationship("Event", back_populates="bookings")