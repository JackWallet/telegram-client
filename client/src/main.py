import logging
import asyncio
from aiogram import Bot
from root.dispatcher import get_dispatcher


logging.basicConfig(
    format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def main() -> None:
    bot = Bot(token="")
    dispatcher = get_dispatcher()
    await dispatcher.start_polling(bot) # type: ignore

if __name__ == "__main__":
    asyncio.run(main())
