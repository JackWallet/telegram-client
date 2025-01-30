import os
from pydantic import ValidationError
from root.exceptions import ConfigException
from root.schema import Config


def get_config() -> Config:
    try:
        return Config(bot_token=os.getenv("BOT_TOKEN"))  # type: ignore
    
    except ValidationError:
        raise ConfigException("Have you provided all required env variables?")
