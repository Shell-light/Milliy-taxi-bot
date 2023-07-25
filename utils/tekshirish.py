
from typing import Union
from aiogram import Bot

async def check(user_id, kanal_link:Union[str,int]):
    bot = Bot.get_current()
    user = await bot.get_chat_member(chat_id=kanal_link, user_id=user_id)
    return user.is_chat_member()
