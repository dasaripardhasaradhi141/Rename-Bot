import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "25993194"))
API_HASH = os.environ.get("API_HASH", "63c16a1e4bec73cc56edbd4e5dbd7a4a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "1278741735"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "DPS_Files")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002048542710"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://dasaripardhasaradhi144:iMVJI3mlBMXAFFDq@cluster0.9l1zaaa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster1")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/1a486a1009c7439b29d1d.jpg")
