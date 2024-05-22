from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery


class CheckSubscriptionMessage(BaseMiddleware):

    async def __call__(
            self, 
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        chat_member = await event.bot.get_chat_member("", event.from_user.id)

        if chat_member.status == "left":
            await event.answer(
                "Подпишись на канал"
            )
        else:
            return await handler(event, data)
        