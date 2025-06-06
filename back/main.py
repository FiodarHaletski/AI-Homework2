from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import List
from datetime import datetime, timedelta

from models import User, get_async_session
from schemas import UserCreate, UserRead, UserUpdate, Token, UserAuth
import crud
import auth

app = FastAPI()

@app.post('/token', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_async_session)):
    user = await crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post('/users/', response_model=UserRead)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_async_session)):
    db_user = await crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud.create_user(db, user)

@app.get('/users/', response_model=List[UserRead])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_async_session), token: str = Depends(auth.oauth2_scheme)):
    await auth.get_current_user(token, db)
    return await crud.get_users(db, skip=skip, limit=limit)

@app.get('/users/{user_id}', response_model=UserRead)
async def read_user(user_id: int, db: AsyncSession = Depends(get_async_session), token: str = Depends(auth.oauth2_scheme)):
    await auth.get_current_user(token, db)
    db_user = await crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put('/users/{user_id}', response_model=UserRead)
async def update_user(user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_async_session), token: str = Depends(auth.oauth2_scheme)):
    await auth.get_current_user(token, db)
    return await crud.update_user(db, user_id, user)

@app.delete('/users/{user_id}', status_code=204)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_async_session), token: str = Depends(auth.oauth2_scheme)):
    await auth.get_current_user(token, db)
    await crud.delete_user(db, user_id)
    return None 