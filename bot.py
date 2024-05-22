import asyncio
from scheduler import Scheduler
from aiogram import Bot, Dispatcher, types
from config.config_reader import config
import motor.motor_asyncio

from handlers import start, dice

client = motor.motor_asyncio.AsyncIOMotorClient(config.base_token.get_secret_value())

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

dp.include_routers(
    start.router,
    dice.router
)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(main())
        loop.run_forever()
    except KeyboardInterrupt:
        pass