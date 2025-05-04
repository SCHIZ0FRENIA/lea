from typing import Optional, List

from pydantic import BaseModel, Field

from .card_schema import Card


class Deck(BaseModel):
    name: str
    description: Optional[str] = None
    created_by: str
    cards: List[Card] = {}