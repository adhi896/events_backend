from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        print("TOKEN RECEIVED:", token)

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("PAYLOAD:", payload)

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token: missing sub"
            )

        return {"user_id": int(user_id)}

    except JWTError as e:
        print("JWT ERROR:", str(e))  # 🔥 THIS LINE IS GOLD
        raise HTTPException(
            status_code=401,
            detail="Token is invalid or expired"
        )