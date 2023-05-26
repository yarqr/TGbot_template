import asyncio

from aiogram import Bot, Dispatcher
from loguru import logger

from mybot.config import settings
from mybot.handlers import client, errors
from mybot.services.commands import set_commands


async def main():
    logger.info('Bot started')

    bot = Bot(settings.BOT_TOKEN)
    dp = Dispatcher()

    await set_commands(bot)
    dp.include_routers(client.router, errors.router)

    await dp.start_polling(bot, close_bot_session=True, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (SystemExit, KeyboardInterrupt):
        logger.error('Bot stopped')
