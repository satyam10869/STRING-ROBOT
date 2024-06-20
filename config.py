from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("21513517"))
API_HASH = getenv("838d3451485b95722878921877f12066")

BOT_TOKEN = getenv("6798222443:AAH7RfDy9QTRJCOBR-IlEXWZ6_PvTgCJATs")
OWNER_ID = int(getenv("5904348755"))

MONGO_DB_URI = getenv("mongodb+srv://sumit333:sumit333@cluster0.emqf08v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("neetumamvol2", None)
