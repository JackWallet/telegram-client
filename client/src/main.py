import logging
import asyncio
from aiogram import Bot
from root.schema import Config
from root.config import get_config
from root.dispatcher import get_dispatcher


logging.basicConfig(
    format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def main() -> None:
    config: Config = get_config()
    bot = Bot(**config.model_dump())
    dispatcher = get_dispatcher()
    
    await dispatcher.start_polling(bot) # type: ignore

if __name__ == "__main__":
    asyncio.run(main())
