import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "11676092"))
API_HASH = getenv("API_HASH", "07cc94d3d8d69851d9f8bac5938a58e7")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6324982798:AAFkm6lbiNh9yVswJrNwDVFAbjqUBzxlieo")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb://clve73lfu001ha4me1al6gw90:UTfT7DjJGjwyvbdXaM1hDrVj@104.251.218.202:9013/?readPreference=primary&ssl=false")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002066328009"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", " 6900132473"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/crazyworld-izzy/1",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TeamHyperNetworks")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Team_Hypers_Networks")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "e60cd7a829cc4a80804553a20c216379")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9d6d953a45b47aea4f56a0acb45ece2")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 5000))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 904857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 9073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQE9p8oACWMBzJnKfVdevbjQqPJGJAGrRYBOxNPXVh9Xt-oS4GGvNJDUPK50PdiUtGaBoZ8isEsBrLXGu6l2cYrwH65Lo7tWf4irvPkLTzqEJqxJ2K8xmUn_ZFV_uU1pJrCil5f7fCA9ffVbdw9quhhxaRx59WeEx-8jANNwWcBQplYUgG6Nx91GwY8C2369VQnBjam3pwYkBIBdNaO05hdH-ve4x2fkOw9U-WtY63cB2d3VKpfOiCQynMLDL4K4DNkNMlkr9mXn5FwHJt7Kev_IQQtjIvmbXX-4fRz_F5ZNUGYdjXp6zLltadUIESjmGNp2A-167O7vce2z65eZ8IFII3jTbwAAAAGSP2H6AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/c59b351a66a77acbf1c98.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/c59b351a66a77acbf1c98.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/c59b351a66a77acbf1c98.jpg"
STATS_IMG_URL = "https://graph.org/file/c59b351a66a77acbf1c98.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/c59b351a66a77acbf1c98.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/c59b351a66a77acbf1c98.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
