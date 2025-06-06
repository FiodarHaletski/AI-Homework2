from pydantic import BaseModel, EmailStr
from typing import Optional

class GeoBase(BaseModel):
    lat: str
    lng: str

class AddressBase(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: GeoBase

class CompanyBase(BaseModel):
    name: str
    catchPhrase: str
    bs: str

class UserBase(BaseModel):
    name: str
    username: str
    email: EmailStr
    address: AddressBase
    phone: str
    website: str
    company: CompanyBase

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class UserAuth(BaseModel):
    email: EmailStr
    password: str 