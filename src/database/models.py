from typing import List
from datetime import datetime
from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship


class Kind(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    pets: List["Pet"] = Relationship(back_populates="kind")


class Pet(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=20)
    born: datetime | None = Field(default=None)
    kind_id: int | None = Field(foreign_key="kind.id")
    kind: Kind = Relationship(back_populates="pets")


class PetRead(BaseModel):
    id: int
    name: str
    born: datetime
    kind: Kind


class KindRead(BaseModel):
    id: int
    name: str
    pets: List[Pet] | None
