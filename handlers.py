import json

from aiogram import Router, F
from aiogram.types import Message, FSInputFile

from keyboards import main_menu, product_nav


router = Router()


# Загружаем товары
with open(
    "products.json",
    "r",
    encoding="utf-8"
) as file:
    products = json.load(file)


# Запоминаем, какой товар смотрит пользователь
user_index = {}



@router.message(F.text == "/start")
async def start(message: Message):

    user_index[message.from_user.id] = 0

    await message.answer(
        "🏪 Welcome to our shop!",
        reply_markup=main_menu()
    )



async def show_product(message: Message):

    user_id = message.from_user.id

    index = user_index.get(user_id, 0)

    product = products[index]


    text = f"""
📦 {product['name']}

💰 Price: {product['price']}

📏 Sizes:
{product['sizes']}

🎨 Colors:
{product['colors']}

📝 Description:
{product['description']}
"""


    photo = FSInputFile(
        product["photo"]
    )


    await message.answer_photo(
        photo=photo,
        caption=text,
        reply_markup=product_nav()
    )



@router.message(F.text == "🛍 Products")
async def products_button(message: Message):

    await show_product(message)



@router.message(F.text == "➡️ Next")
async def next_product(message: Message):

    user_id = message.from_user.id


    index = user_index.get(
        user_id,
        0
    )


    index += 1


    if index >= len(products):
        index = 0


    user_index[user_id] = index


    await show_product(message)



@router.message(F.text == "⬅️ Back")
async def previous_product(message: Message):

    user_id = message.from_user.id


    index = user_index.get(
        user_id,
        0
    )


    index -= 1


    if index < 0:
        index = len(products)-1


    user_index[user_id] = index


    await show_product(message)



@router.message(F.text == "🛒 Buy")
async def buy(message: Message):

    await message.answer(
        """
💳 Payment details:

MBank:
0000 0000 0000


☎️ Phone:
+996 XXX XX XX XX


After payment send a receipt.
"""
    )



@router.message(F.text == "📍 Shop Address")
async def address(message: Message):

    await message.answer(
        """
📍 Our address:

Bishkek
Kyrgyzstan

Working hours:
09:00 - 20:00
"""
    )



@router.message(F.text == "ℹ️ About the Shop")
async def about(message: Message):

    await message.answer(
        """
🏪 About our shop:

We sell quality shoes.

✅ Good prices
✅ Modern models
✅ Fast delivery
"""
    )