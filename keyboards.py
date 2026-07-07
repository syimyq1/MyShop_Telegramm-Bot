from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():

    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🛍 Products")],
            [KeyboardButton(text="📍 Shop Address")],
            [KeyboardButton(text="ℹ️ About the Shop")]
        ],
        resize_keyboard=True
    )


def product_nav():

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="⬅️ Back"),
                KeyboardButton(text="🛒 Buy"),
                KeyboardButton(text="➡️ Next")
            ]
        ],
        resize_keyboard=True
    )
