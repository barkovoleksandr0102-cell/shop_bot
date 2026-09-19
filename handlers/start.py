from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command(commands=["start"]))
async def start_handler(message: Message):
    await message.answer(
        text=f"Hello, {message.from_user.first_name}! I am your bot. How can I assist you today?"
    )