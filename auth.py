from datetime import datetime, timedelta
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
import os 

SECRET_KEY = os.environ["SECRET_KEY"]
ACCESS_PSW = os.environ['ACCESS_PSW']


class Token(BaseModel):
    access_token: str
    token_type: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_psw(psw):
    return psw == ACCESS_PSW

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta (minutes=45)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    
    return encoded_jwt
