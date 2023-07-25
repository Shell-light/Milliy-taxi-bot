from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


shartlar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💬Telegram guruh", url="https://t.me/senservischat"),
            InlineKeyboardButton(text="📷Instagram", url="https://www.instagram.com/milliy_taksi/")
        ],
        [
            InlineKeyboardButton(text="🔗Ulashish", switch_inline_query="botga a'zo boling. Konkursda ishtirok etib 1000$ mukofotini qo'lga kiriting"),
            InlineKeyboardButton(text="🧩Play Market",url="https://play.google.com/store/apps/details?id=uz.bdmgroup.milliy_taxi_client")

        ],
        [
            InlineKeyboardButton(text="✅Tasdiqlash", callback_data='tasdiqlash')
        ]
    ]
)

