from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startkey import startbut
from loader import dp, bot
from data.config import ADMINS



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    await message.answer(f"Assalomu Aleykum Hurmatli, {message.from_user.full_name}!\nSiz botimizning 567 chi foydalanuvchisi siz\nsiz uchun maxsus 🎁BONUS🎁 lar mavjud",reply_markup=startbut)

