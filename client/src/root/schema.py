from pydantic import BaseModel

class Config(BaseModel):
    bot_token: str