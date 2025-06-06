from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from passlib.context import CryptContext
from models import User, AuthUser, Address, Company, Geo
from schemas import UserCreate, UserUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email).options(selectinload(User.address).selectinload(Address.geo), selectinload(User.company)))
    return result.scalars().first()

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id).options(selectinload(User.address).selectinload(Address.geo), selectinload(User.company)))
    return result.scalars().first()

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(User).options(selectinload(User.address).selectinload(Address.geo), selectinload(User.company)).offset(skip).limit(limit))
    return result.scalars().all()

async def create_user(db: AsyncSession, user: UserCreate):
    geo = Geo(lat=user.address.geo.lat, lng=user.address.geo.lng)
    db.add(geo)
    await db.flush()
    address = Address(street=user.address.street, suite=user.address.suite, city=user.address.city, zipcode=user.address.zipcode, geo=geo)
    db.add(address)
    await db.flush()
    company = Company(name=user.company.name, catchPhrase=user.company.catchPhrase, bs=user.company.bs)
    db.add(company)
    await db.flush()
    db_user = User(name=user.name, username=user.username, email=user.email, address=address, phone=user.phone, website=user.website, company=company)
    db.add(db_user)
    await db.flush()
    password_hash = pwd_context.hash(user.password)
    db_auth = AuthUser(name=user.name, email=user.email, password_hash=password_hash)
    db.add(db_auth)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def update_user(db: AsyncSession, user_id: int, user: UserUpdate):
    db_user = await get_user(db, user_id)
    if not db_user:
        return None
    db_user.name = user.name
    db_user.username = user.username
    db_user.email = user.email
    db_user.phone = user.phone
    db_user.website = user.website
    db_user.address.street = user.address.street
    db_user.address.suite = user.address.suite
    db_user.address.city = user.address.city
    db_user.address.zipcode = user.address.zipcode
    db_user.address.geo.lat = user.address.geo.lat
    db_user.address.geo.lng = user.address.geo.lng
    db_user.company.name = user.company.name
    db_user.company.catchPhrase = user.company.catchPhrase
    db_user.company.bs = user.company.bs
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def delete_user(db: AsyncSession, user_id: int):
    db_user = await get_user(db, user_id)
    if db_user:
        await db.delete(db_user)
        await db.commit()

async def authenticate_user(db: AsyncSession, email: str, password: str):
    result = await db.execute(select(AuthUser).where(AuthUser.email == email))
    user = result.scalars().first()
    if not user:
        return None
    if not pwd_context.verify(password, user.password_hash):
        return None
    return await get_user_by_email(db, email) 