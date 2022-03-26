# from cgitb import text
from email import message
from email.message import Message
from aiogram.dispatcher.filters import Command,Text
from telegram import CallbackQuery, ReplyMarkup
from keyboards.default.socials import contact,startnak
from keyboards.default.startkey import startbut
from keyboards.inline.avtor import SHARIF
from aiogram import Bot
from aiogram import types 
from aiogram.dispatcher import filters
from data.config import BOT_TOKEN,ADMINS
# from states.sss import PersonalData
# from data.config import BOT_TOKEN
from loader import dp, bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.inline.avtor import FOLLOWER_INSTA

# bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)


PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


@dp.message_handler(text="Ro`yxatdan O`tish")
async def sharif(message: Message):
    await message.answer(f"Nakrutka off xizmatidan foydalanish uchun kontakt yuboring", reply_markup=contact)
    # await message.answer(f"Bo`limlardan birini tanlang",reply_markup =startnak)


@dp.message_handler(content_types="contact")
async def sharif(message: Message):
    await message.answer(f"Kontakt qabul qilindi", reply_markup=startnak)
    await bot.send_message(ADMINS[0], message)
    


@dp.message_handler(text="Admin bilan Bog`lanish")
async def show_menu(message: Message):
    
    await message.answer(f"salom")

@dp.message_handler(text="🕸 Instagram 🕸")
async def show_instagram(message: Message):
    global followers
    followers = 0
    await message.answer("Instagramdagi Obunachilar sonini tanlang👤")
    await message.answer(f"Instagram 👤obunachilar👤 soni:{followers}",reply_markup = FOLLOWER_INSTA)
@dp.callback_query_handler(text = "ayrish")
async def qoshish(call: CallbackQuery):
    global followers
    followers -=1000
    await call.message.delete()
    await call.message.answer(f"Instagram 👤obunachilar👤 soni:{followers}",reply_markup = FOLLOWER_INSTA)
@dp.callback_query_handler(text = "qoshish")
async def ayrish(call: CallbackQuery):
    global followers
    followers +=1000
    await call.message.delete()
    await call.message.answer(f"Instagram 👤obunachilar👤 soni:{followers}",reply_markup = FOLLOWER_INSTA)
@dp.callback_query_handler(text = "Tasdiqlash")
async def tasdiqlash(call: CallbackQuery):
    global followers
    natija = followers * 18
    await call.message.delete()
    await call.message.answer(f"Buyurtma narxi: {natija}USZ")
    

