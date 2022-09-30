import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("8663240"))
    API_HASH = os.environ.get("bb30f6409dfe5b12b044a61ddd3abed6")
    BOT_TOKEN = os.environ.get("5725115261:AAFRktdtcxuK7FGQfbeukZBEvGZi9KrH7Qs")
    BOT_USERNAME = os.environ.get("link_biltayx_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
