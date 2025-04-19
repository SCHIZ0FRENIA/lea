import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    port = int(os.getenv("PORT", 3000))
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY")

    if not SECRET_KEY:
        raise ValueError("There are no SECRET_KEY var provided in the environment")

    MONGO_URI = os.getenv("MONGO_URI")

    if not MONGO_URI:
        raise ValueError("There are no MONGO_URI var provided in the environment")

    DB_NAME = os.getenv("DB_NAME", "lea_db")
    USERS_COLLECTION_NAME = "users"
