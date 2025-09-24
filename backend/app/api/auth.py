from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..models.user import UserCreate, UserInDB, Token
from ..utils.auth import create_access_token, get_current_user, verify_password, get_password_hash
from ..database import db
from datetime import timedelta

router = APIRouter()

@router.post("/register", response_model=UserInDB)
def register(user: UserCreate):
    db_user = db.users.find_one({"email": user.email})
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    hashed_password = get_password_hash(user.password)
    user_in_db = UserInDB(**user.dict(), hashed_password=hashed_password)
    db.users.insert_one(user_in_db.dict())
    return user_in_db

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.users.find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
