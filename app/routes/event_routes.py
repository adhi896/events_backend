from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..database import AsyncSessionLocal
from ..models.event_model import Event
from ..models.booking_model import Booking
from ..schemas.booking_schema import BookingResponse, BookingCreate
from ..auth import verify_token
from sqlalchemy.orm import selectinload



router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


@router.get("/events")
async def get_events(
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(verify_token)
):
    try:
        result = await db.execute(select(Event))
        events = result.scalars().all()

        if not events:
            return {
                "message": "No events found",
                "data": []
            }

        return {
            "message": "Events fetched successfully",
            "data": events
        }

    except Exception as e:
        # Log error in real projects
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching events: {str(e)}"
        )
    


@router.post("/book-event", response_model=BookingResponse)
async def book_event(
    booking: BookingCreate,
    db: AsyncSession = Depends(get_db),
    user=Depends(verify_token)
):
    try:
        user_id = user["user_id"]
        event_id = booking.event_id

        result = await db.execute(
            select(Event).where(Event.id == event_id)
        )
        event = result.scalar_one_or_none()

        if not event:
            raise HTTPException(
                status_code=404,
                detail="Event not found"
            )

        result = await db.execute(
            select(Booking).where(
                Booking.user_id == user_id,
                Booking.event_id == event_id
            )
        )
        existing_booking = result.scalar_one_or_none()

        if existing_booking:
            raise HTTPException(
                status_code=400,
                detail="You have already booked this event"
            )

        new_booking = Booking(
            user_id=user_id,
            event_id=event_id
        )

        db.add(new_booking)
        await db.commit()
        await db.refresh(new_booking)

        return new_booking

    except HTTPException:
        raise

    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.get("/my-bookings")
async def get_my_bookings(
    db: AsyncSession = Depends(get_db),
    user=Depends(verify_token)
):
    try:
        user_id = user["user_id"]

        result = await db.execute(
            select(Booking)
            .options(selectinload(Booking.event))  
            .where(Booking.user_id == user_id)
        )

        bookings = result.scalars().all()

        # Format response nicely
        data = []
        for b in bookings:
            data.append({
                "booking_id": b.id,
                "event_id": b.event.id,
                "event_name": b.event.name,
                "location": b.event.location,
                "event_time": b.event.event_time,
                "booked_at": b.created_at
            })

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))