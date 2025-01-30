from aiogram import Router
from aiogram.types.message import Message
from aiogram.filters.command import CommandStart

web_app_router = Router(name=__name__)

@web_app_router.message(CommandStart(), flags={"rate_limit": {"rate": 5}})
async def handle_start(message: Message) -> Message:
    return await message.answer(text="Hello")