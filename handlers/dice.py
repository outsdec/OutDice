from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message, CallbackQuery
from config.config_reader import config
from database.database import Database

db = Database()

bot = Bot(config.bot_token.get_secret_value())

router = Router()  # [1]

@router.message(Command("dice"))
async def roll_dice(message: types.Message):
    data = await bot.send_dice(message.chat.id, emoji='🎲')
    await message.answer(f'значение кубика {data.dice.value}')
