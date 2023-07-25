from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.inline.dostlarga_yuborish import send_friend_buttons
from loader import dp, bot, base


from keyboards.inline.ishtirok_uchun import inline_ishtirok_buttons
from keyboards.inline.shartlar_uchun import shartlar_buttons

# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!")
from states.holatlar import Form


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    ismi = message.from_user.first_name
    familyasi = message.from_user.last_name
    usernamei = message.from_user.username
    user_id = message.from_user.id
    try:
        base.user_qoshish(ism=ismi, tg_id=user_id, fam=familyasi, username=usernamei)
    except Exception:
        pass
    user_id = message.from_user.id
    rasm_manzili = 'https://t.me/audiowiki/5'
    await bot.send_photo(chat_id=user_id, photo=rasm_manzili, caption="  Assalomu alaykum !!! \nMilliy taksi konkursiga xush kelibsiz ! \nKonkursda ishtirok eting va g'olib bo'ling. \nBosh sovrin 1000$ pul mukofoti.", reply_markup=inline_ishtirok_buttons)


@dp.callback_query_handler(text = 'ishtirok')
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"""
Quyidagi shartlarni to'liq bajaring va konkurs ishtirokchisiga aylaning. Shartlar:
✅ Telegram guruhga a'zo bo'ling va 50ta do'stingizni qo'shing
✅ Instagram sahifamizga a'zo bo'ling va barcha postlarga layk bosing
✅ Play marketdan "Milliy taxi" ilovasini yuklab oling va ilova orqali taksiga buyurtma bering
✅ Ushbu konkurs botni 3ta guruhga va 20 do'stingizga yuboring

""", reply_markup=shartlar_buttons)

@dp.callback_query_handler(text = 'tasdiqlash')
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(text="Siz telefon raqamingizni yuborish orqli to'liq ro'yhatdan o'tishingiz mumkin.")
    await Form.tel_holati.set()


@dp.message_handler(state=Form.tel_holati)
async def bot_start(message: types.Message, state:FSMContext):
    nomer = message.text
    await state.update_data({"tel": nomer})
    malumot = await state.get_data()
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    tel = malumot.get('tel')
    username = message.from_user.username
    tg_id = message.from_user.id
    text = f"👤 Ism : {ism}\n" \
           f"👤Familya:  {familya}\n" \
           f"📱Telefon raqami : {tel}\n" \
           f"🌐Telegram : @{username}\n"
    await message.answer(f"Tabriklaymiz siz Milliy taksi konkursi ishtirokchisiga aylandingiz !!! "
                         f"Konkurs g'oliblari Tezkunda instagram sahifamiz va telegram "
                         f"guruhimiz jonli efirida konkurs ishtirokchilari va Milliy taksi "
                         f"mijozlari orasidan aniqlanadi. "
                         f"Bu yangilikni qancha ko'p do'stingizga "
                         f"yuborsangiz va Milliy taksidan qancha ko'p foydalansangiz yutish imkonoyatingiz "
                         f"shuncha ko'p bo'ladi. Bosh sovrin 1000$", reply_markup=send_friend_buttons)
    await bot.send_message(chat_id='789362160', text=text)
    await state.finish()


@dp.message_handler(commands = 'reklama',chat_id='789362160')
async def bot_start(message: types.Message):
    userlar = base.select_all_foydalanuvchilar()
    for user in userlar:
        await bot.send_message(chat_id=user[4], text='Bu reklama')


@dp.message_handler(commands="sanash", chat_id='789362160')
async def bot_start(message: types.Message):
    sanash = base.sanash_foydalanuvchilar()
    guruh_id = message.from_user.id
    for sana in sanash:
        await bot.send_message(chat_id=guruh_id, text=f"{sanash[0]} ta foydalanuvchi bor")


@dp.message_handler(commands = ['light', 'Light', 'LIGHT'])
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='光からのご挨拶')

