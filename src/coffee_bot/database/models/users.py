from sqlalchemy.orm import Mapped
from .base import Base


class User(Base):
    first_name: Mapped[str]
    second_name: Mapped[str]
    last_name: Mapped[str]
    position: Mapped[str]
    group: Mapped[str]
    user_id: Mapped[int]

