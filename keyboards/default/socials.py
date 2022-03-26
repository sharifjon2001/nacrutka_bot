# from cgitb import text
import types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiohttp import request
# from sqlalchemy import true
# from telegram import Contact
startnak = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "🕸 Instagram 🕸"),
            KeyboardButton(text = "🕸 You Tube 🕸"),
        ],
        
        [
            KeyboardButton(text = "🕸 Tik Tok 🕸"),
            KeyboardButton(text = "🕸 Telegram 🕸"),
        ],
        
    ],
    resize_keyboard=True,
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text= "Kontakt yuboring📞",request_contact=True)
        ],
    ],
    resize_keyboard=True,
)