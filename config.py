import os

ENVIRONMENT = os.environ.get("ENVIRONMENT", "ANYTHING")

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get("API_ID", 6))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get("API_HASH", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("SCALINGO_POSTGRESQL_URL", None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    OWNER_ID = os.environ.get("OWNER_ID", "5502537272")
    MUST_JOIN = os.environ.get("MUST_JOIN", "Repthon")
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "Repthon")
else:
    # Fill the Values
    API_ID = 6
    API_HASH = ""
    BOT_TOKEN = ""
    DATABASE_URL = ""
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    OWNER_ID = "5502537272"
    MUST_JOIN = "Repthon"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
