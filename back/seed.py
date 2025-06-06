import asyncio
import json
from sqlalchemy.ext.asyncio import AsyncSession
from models import Base, engine, async_session, Geo, Address, Company, User, AuthUser
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with async_session() as session:
        with open('users_seed.json', 'r') as f:
            users = json.load(f)
        for u in users:
            geo = Geo(lat=u['address']['geo']['lat'], lng=u['address']['geo']['lng'])
            session.add(geo)
            await session.flush()
            address = Address(street=u['address']['street'], suite=u['address']['suite'], city=u['address']['city'], zipcode=u['address']['zipcode'], geo=geo)
            session.add(address)
            await session.flush()
            company = Company(name=u['company']['name'], catchPhrase=u['company']['catchPhrase'], bs=u['company']['bs'])
            session.add(company)
            await session.flush()
            user = User(name=u['name'], username=u['username'], email=u['email'], address=address, phone=u['phone'], website=u['website'], company=company)
            session.add(user)
            await session.flush()
            password_hash = pwd_context.hash('password')
            auth_user = AuthUser(name=u['name'], email=u['email'], password_hash=password_hash)
            session.add(auth_user)
        await session.commit()

if __name__ == '__main__':
    asyncio.run(seed()) 