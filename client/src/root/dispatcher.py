from aiogram import Dispatcher
from web_application.router import web_app_router


def get_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_routers(web_app_router)
    return dp