from datetime import datetime
from pydantic import BaseModel



class BookingResponse(BaseModel):
    id: int
    user_id: int
    event_id: int
    created_at: datetime

    class Config:
        from_attributes = True  


class BookingCreate(BaseModel):
    event_id: int