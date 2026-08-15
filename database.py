from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Text


DATABASE_URL = "sqlite+aiosqlite:///AghaKocholo.db"


engine = create_async_engine(
    DATABASE_URL,
    echo=False
)


async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


Base = declarative_base()


# 👤 کاربران
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    telegram_id = Column(
        Integer,
        unique=True
    )

    username = Column(
        String,
        nullable=True
    )


# 💎 پلن ها
class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    location = Column(String)

    volume = Column(String)

    price = Column(Integer)


# 🛒 سفارش ها
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    plan_id = Column(Integer)

    status = Column(String)

    receipt = Column(Text)

    config = Column(Text)


async def init_db():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )
