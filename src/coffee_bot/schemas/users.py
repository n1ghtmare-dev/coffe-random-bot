from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    first_name: str | None
    second_name: str | None
    last_name: str | None
    position: str | None
    group: str | None
    user_id: int


class UserCreate(UserBase):
    pass

class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


