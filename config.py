import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH") or None

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID"))

MONGO_DB_URI = os.environ.get("SCALINGO_MONGO_URL", None)
MUST_JOIN = getenv("MUST_JOIN", "Repthon")

PORT = os.environ.get("PORT", None)
