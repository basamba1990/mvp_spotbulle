from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token")
async def login():
    # Implementation à compléter
    return {"token": "fake-token"}

@router.post("/register")
async def register():
    # Implementation à compléter
    return {"message": "User created"}
