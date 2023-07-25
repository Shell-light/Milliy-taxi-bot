from aiogram import types
from aiogram.types import ContentType
from loader import dp, bot


from filters.guruhlar_uchun import Guruh
# Echo bot5
@dp.message_handler(Guruh(),commands="start")
async def bot_echo(message: types.Message):
    await message.answer("Guruhga hush kelibsiz")


# @dp.message_handler(Guruh(),text=["Salom", "salom"])
# async def bot_echo(message: types.Message):
#     await message.reply(text="Assalomu allaykum!")


@dp.message_handler(Guruh(), content_types=ContentType.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    ism = message.new_chat_members[0].first_name
    msg = message.message_id
    guruh_id = message.chat.id
    await message.reply(text=f"Assalomu allaykum! {ism}")
    await message.bot.delete_message(chat_id=guruh_id, message_id=msg)

# @dp.message_handler(Guruh(), content_types=ContentType.LEFT_CHAT_MEMBER)
# async def bot_echo(message: types.Message):
#     ism = message.left_chat_member.first_name
#     msg = message.message_id
#     guruh_id = message.chat.id
#     await message.reply(text=f"Guruhni tark etdi! {ism}")
#     await message.bot.delete_message(chat_id=guruh_id, message_id=msg)

#
# @dp.message_handler(Guruh(),text=["Dam", "dam"])
# async def bot_echo(message: types.Message):
#     user_id = message.from_user.id
#     ism = message.from_user.first_name
#     guruh_id = message.chat.id
#     await message.bot.restrict_chat_member(chat_id=guruh_id, user_id=user_id, until_date="2")
#     await message.reply(text=f"{ism} bloklandi")