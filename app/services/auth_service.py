from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models.user_model import User
from ..utils.password import hash_password, verify_password
from ..utils.jwt_handler import create_access_token


async def register_user(db: AsyncSession, user):

    new_user = User(
        name=user.name,
        phone=user.phone,
        password=user.password
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


async def login_user(db: AsyncSession, user):

    result = await db.execute(
        select(User).where(User.phone == user.phone)
    )

    db_user = result.scalar_one_or_none()

    if not db_user:
        return None

    if not user.password == db_user.password:
        return None

    token = create_access_token({"sub": str(db_user.id)})

    return token