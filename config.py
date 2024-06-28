import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.environ.get("API_ID", 6))
API_HASH = os.environ.get"API_HASH")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OWNER_ID = int(os.environ.get("OWNER_ID", None))

MONGO_DB_URI = os.environ.get("SCALINGO_MONGODB_URL", None)
MUST_JOIN = os.environ.get("MUST_JOIN", "Repthon")

PORT = os.environ.get("PORT", None)
