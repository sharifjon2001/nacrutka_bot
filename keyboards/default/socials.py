# from cgitb import text
import types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiohttp import request
# from sqlalchemy import true
# from telegram import Contact
startnak = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "๐ธ Instagram ๐ธ"),
            KeyboardButton(text = "๐ธ You Tube ๐ธ"),
        ],
        
        [
            KeyboardButton(text = "๐ธ Tik Tok ๐ธ"),
            KeyboardButton(text = "๐ธ Telegram ๐ธ"),
        ],
        
    ],
    resize_keyboard=True,
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text= "Kontakt yuboring๐",request_contact=True)
        ],
    ],
    resize_keyboard=True,
)