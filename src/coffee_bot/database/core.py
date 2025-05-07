from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import async_scoped_session, async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base 
from pathlib import Path 
from contextlib import asynccontextmanager
from asyncio import current_task
from config import settings 



BASE_DIR = Path(__file__).resolve().parent.parent.parent

Base = declarative_base()

class DatabaseManager:
    def __init__(self, url: str) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=True,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    @asynccontextmanager
    async def session(self):
        async with self.session_factory() as session:
            yield session

    async def create_tables(self, Base):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
                

db_manager = DatabaseManager(url=settings.DB_URL)

