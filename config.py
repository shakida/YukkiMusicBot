from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
STRING = getenv("STRING_SESSION", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = "2382418" # int(getenv("API_ID", "2382418"))
API_HASH = getenv("API_HASH")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = "mongodb+srv://shakida:RR69pro@zoz.qvta8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority" # getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001410806326"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")
if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))
