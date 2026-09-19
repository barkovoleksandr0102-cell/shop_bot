from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
import keyboards.back_to as kb
from database.users_db import DB as db

router = Router()

@router.callback_query(F.data == "profile")
async def profile_handler(message: CallbackQuery):
    user = db.get_user(user_id=message.from_user.id)
    balance = user[3] if user else 0
    access_level = user[4] if user else 0
    await message.message.edit_text(text=f"""
👤 <b>Профиль пользователя</b>
🏷 <b>Username:</b> {message.from_user.username}
💰 <b>Баланс:</b> {balance} грн.
🔑 <b>Уровень доступа:</b> {access_level}""")
    await message.message.edit_reply_markup(reply_markup=kb.return_kb(to="menu"))