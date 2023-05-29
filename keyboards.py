from aiogram import types 
async def start_menu_btn():
    message = types.Message
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(
        types.KeyboardButton("🖇 Ro'yxatdan o'tish"),

        types.KeyboardButton("👤 Admin bilan aloqa"),
    )
    return btn


async def info_yes_or_no_btn():
    btn = types.InlineKeyboardMarkup()
    btn.add(
        types.InlineKeyboardButton("✅", callback_data="yes"),
        types.InlineKeyboardButton("❎", callback_data="no"),
    )

    return btn