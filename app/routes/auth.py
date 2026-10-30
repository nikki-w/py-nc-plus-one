import jwt
import os
from fastapi import APIRouter, HTTPException
from datetime import datetime, timezone, timedelta
from pydantic import BaseModel
from app.models.users import get_user, register_user, check_if_email_exists
from src.passwords import verify_password

auth_router = APIRouter(prefix="/auth")

ALGORITHM = "HS256"

class LoginRequest(BaseModel):
    email: str
    password: str


class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str


def get_secret():
    return os.getenv("JWT_SECRET")


def create_access_token(id: int) -> str:
    payload = {
        "sub": str(id),
        "exp": datetime.now(timezone.utc) + timedelta(hours=4)
    }
    return jwt.encode(payload, get_secret(), algorithm=ALGORITHM)


@auth_router.post("/login")
def login(body: LoginRequest):
    if not body.email or body.email == "":
         raise HTTPException(
            status_code=400, 
            detail="Email is required."
        )       

    if not body.password or body.password == "":
         raise HTTPException(
            status_code=400, 
            detail="Password is required."
        )       


    user = get_user(body.email)

    if not user:
        raise HTTPException(
            status_code=401, 
            detail="Incorrect email or password"
        )

    if verify_password(body.password, user["password_hash"]):
        return {
            "access_token": create_access_token(user["id"]),
            "token_type": "bearer"
        }
        
    raise HTTPException(
        status_code=401, 
        detail="Incorrect email or password"
    )


@auth_router.post("/register", status_code=201)
def register(body: RegisterRequest):

    if not body.name or body.name == "":
         raise HTTPException(
            status_code=400, 
            detail="Name is required."
        )       

    if not body.email or body.email == "":
         raise HTTPException(
            status_code=400, 
            detail="Email is required."
        )       

    if not body.password or body.password == "":
         raise HTTPException(
            status_code=400, 
            detail="Password is required."
        )       

    if check_if_email_exists(body.email):
         raise HTTPException(
            status_code=409, 
            detail="Email is already in use."
        )       

    new_user = register_user(body.name, body.email, body.password)
    return new_user