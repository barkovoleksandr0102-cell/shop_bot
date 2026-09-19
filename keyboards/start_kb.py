from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_kb() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text="🛍 Каталог", callback_data="catalog")
    builder.button(text="🛒 Корзина", callback_data="cart")
    builder.button(text="📦 Мои заказы", callback_data="orders")
    builder.button(text="👤 Профиль", callback_data="profile")
    builder.button(text="ℹ️ О магазине", callback_data="about")
    builder.adjust(1, 2, 2)
    return builder.as_markup()