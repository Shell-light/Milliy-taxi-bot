import aiogram
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot
from data.config import kanallar
from utils.tekshirish import check

class Asosiy_checking(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,date:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = "Bot ishlashi uchun quyidagi kanllarga a'zo bo'ling\n"
        buttun = []
        dastlabki_holat = True # True ==1 False == 0
        for kanal in kanallar:
            holat = await check(user_id=user_id, kanal_link=kanal)
            dastlabki_holat *= holat

            kanal = await bot.get_chat(kanal)
            if not holat:
                link = await kanal.export_invite_link()
                buttun.append(InlineKeyboardButton(text=kanal.title, url=link))
        if not dastlabki_holat:

            await bot.send_message(chat_id=user_id,disable_web_page_preview=True,text=matn,reply_markup=InlineKeyboardMarkup(inline_keyboard=[buttun]))
            raise CancelHandler()
