from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
import keyboards.start_kb as kb
from database.users_db import DB as db


router = Router()

@router.callback_query(F.data.startswith("back_to:"))
async def back_to_handler(message: CallbackQuery):
    to = message.data.split(":")[1]
    if to == "menu":
        await message.message.edit_text(
            text="""
👋 <b>Добро пожаловать в наш магазин!</b>

Здесь ты можешь найти одежду на любой вкус 👕✨

🛍 <b>Что можно сделать:</b>
• посмотреть каталог товаров
• выбрать размер и цвет
• добавить товары в корзину
• оформить заказ
• отслеживать свои заказы

👇 <b>Выбери нужный раздел:</b>"""
        )
        await message.message.edit_reply_markup(reply_markup=kb.start_kb())