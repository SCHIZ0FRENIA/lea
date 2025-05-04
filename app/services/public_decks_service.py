from ..utils.exceptions.database_exception import DatabaseException
from ..utils.exceptions.lea_exception import LeaException


class PublicDecksService:
    def __init__(self, db):
        self.db = db

    def create_public_deck(self, deck):

        if not deck.name:
            raise LeaException("Deck's name is empty")

        if not deck.created_by:
            raise LeaException("Deck's creator can't be empty")

        if len(deck.description) > 255:
            raise LeaException("Deck's description is too long")

        check_result = self.db.public_decks.find_one({
            "name": deck.name,
            "description": deck.description,
            "created_by": deck.created_by,
        })

        if check_result:
            raise DatabaseException("The same deck already exists")

        insert_result = self.db.public_decks.insert_one(
            deck.dict(by_alias=True)
        )

        return insert_result