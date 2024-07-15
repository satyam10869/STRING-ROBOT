from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("22439323"))
API_HASH = getenv("e0e203c8be2c2c58b04d0c59fc82f507")

BOT_TOKEN = getenv("7027698696:AAFsRd9A3nwQwfQWCBUu3iYGsUPNP1RWLco")
OWNER_ID = int(getenv("7328902365"))

MONGO_DB_URI = getenv("mongodb+srv://satyamyt10869:Sumit10869@cluster0.0ojjo0p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("neetumamvol_2", None)
