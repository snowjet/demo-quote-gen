from typing import List, Optional
from pydantic import BaseModel


class QuotesBase(BaseModel):
    name: str
    quote: str


class QuotesCreate(QuotesBase):
    pass


class Quote(QuotesBase):
    id: int
    name: str
    quote: str

    class Config:
        orm_mode = True
