from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import keyboards.start_kb as kb
from database.users_db import DB as db


router = Router()


@router.message(Command(commands=["start"]))
async def start_handler(message: Message):
    await message.answer(reply_markup=kb.start_kb(),
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

    db.add_user(user_id=message.from_user.id, username=message.from_user.username)