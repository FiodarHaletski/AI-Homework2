from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+asyncpg://user:password@localhost:5432/usersdb')

Base = declarative_base()
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

def get_async_session():
    session = async_session()
    try:
        yield session
    finally:
        session.close()

class Geo(Base):
    __tablename__ = 'geos'
    id = Column(Integer, primary_key=True, index=True)
    lat = Column(String, nullable=False)
    lng = Column(String, nullable=False)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, nullable=False)
    suite = Column(String, nullable=False)
    city = Column(String, nullable=False)
    zipcode = Column(String, nullable=False)
    geo_id = Column(Integer, ForeignKey('geos.id'))
    geo = relationship('Geo')

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    catchPhrase = Column(String, nullable=False)
    bs = Column(String, nullable=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    address_id = Column(Integer, ForeignKey('addresses.id'))
    address = relationship('Address')
    phone = Column(String, nullable=False)
    website = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship('Company')

class AuthUser(Base):
    __tablename__ = 'auth_users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False) 