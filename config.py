import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1614302003:AAHxJ6bPjvcmBzPKGP9qdR9n__1mdoem5g0")

    APP_ID = int(os.environ.get("APP_ID", 6))

    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
