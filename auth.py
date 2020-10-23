from datetime import datetime, timedelta
from pydantic import BaseModel
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import os

SECRET_KEY = os.environ["SECRET_KEY"]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_token(data: dict):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=45)
    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return encoded_jwt


def verify_token(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        if payload["admin"] == "verte":
            return payload["admin"]
        else:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
