from pydantic import BaseModel


class Card(BaseModel):
    id: str
    front: str
    back: str