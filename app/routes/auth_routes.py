from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.user_schema import UserCreate, UserLogin
from ..services.auth_service import register_user, login_user
from ..dependencies import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await register_user(db, user)


@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    
    token = await login_user(db, user)

    if not token:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user found. Please register an account."
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }