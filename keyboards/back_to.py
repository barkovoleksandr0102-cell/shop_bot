from aiogram.utils.keyboard import InlineKeyboardBuilder


def return_kb(to) -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text="◀ Назад", callback_data=f"back_to:{to}")
    return builder.as_markup()