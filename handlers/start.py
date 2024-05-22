from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message, CallbackQuery
from aiogram.utils.deep_linking import create_start_link, decode_payload
from config.config_reader import config
from database.database import Database
db = Database()
bot = Bot(config.bot_token.get_secret_value())

router = Router()  # [1]

@router.message(Command("start"))
async def cmd_start(message: Message, command: CommandObject, bot: Bot):
    user_id = message.from_user.id
    args = command.args
    success, error_message = await db.register_user(user_id)
    if success:
        await message.reply("Привет! Ты успешно зарегистрирован.")
#   if args:
#       payload = decode_payload(args)
#       refer = await find_user(payload)
#       referall = await find_user(user_id)
#       if(refer == referall):
#           return
#       await find_user(user_id)
#       await message.answer(f'Вас пригласил {(refer["nickname"])}')
#       await bot.send_message(chat_id=refer["_id"], text=f'Вы успешно пригласили {referall["nickname"]}')