import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = "8425777888:AAGLs-byCn-1PaBqk0l37in3Aac_aTbri0A"

dp = Dispatcher()


# ASOSIY MENYU
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Janggovor"), KeyboardButton(text="Ramantik")],
        [KeyboardButton(text="Serial"), KeyboardButton(text="Ujis")]
    ],
    resize_keyboard=True
)


# JANGGOVOR MENYU
jang_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Alfa"), KeyboardButton(text="Qasoskorlar")],
        [KeyboardButton(text="JonUki"), KeyboardButton(text="Transformerlar")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)


# QASOSKORLAR MENYU
qasos_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Qasoskorlar-1"), KeyboardButton(text="Qasoskorlar-2")],
        [KeyboardButton(text="Qasoskorlar-3"), KeyboardButton(text="Qasoskorlar-4")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)


# TRANSFORMERLAR MENYU
transformer_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Transformerlar 1")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)


# JONUKI MENYU
jonuki_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="JonUki 1"), KeyboardButton(text="JonUki 2")],
        [KeyboardButton(text="Ortga")]
    ],
    resize_keyboard=True
)


# START
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Salom! Xush kelibsiz Kinolar Olami!",
        reply_markup=menu
    )


# JANGGOVOR
@dp.message(F.text == "Janggovor")
async def janggovor(message: Message):
    await message.answer(
        "🎬 Janggovar Filmlar",
        reply_markup=jang_button
    )


# ALFA
@dp.message(F.text == "Alfa")
async def alfa(message: Message):
    await message.answer(
        "🎬 Nomi: Bio qurol Alfa\n"
        "🌍 Tili: O'zbek tilida\n"
        "📀 Sifati: 720P HD\n"
        "🌏 Davlat: AQSH\n"
        "📆 Yili: 2022-yil\n\n"
        "🎥 https://t.me/Kinolark/9472",
        reply_markup=jang_button
    )


# QASOSKORLAR
@dp.message(F.text == "Qasoskorlar")
async def qasoskorlar(message: Message):
    await message.answer(
        "🎬 Qasoskorlar Filmlar",
        reply_markup=qasos_button
    )


# TRANSFORMERLAR
@dp.message(F.text == "Transformerlar")
async def transformerlar(message: Message):
    await message.answer(
        "🎬 Transformerlar Filmlar",
        reply_markup=transformer_button
    )


# JONUKI
@dp.message(F.text == "JonUki")
async def jonuki(message: Message):
    await message.answer(
        "🎬 JonUki Filmlar",
        reply_markup=jonuki_button
    )


# QASOSKORLAR FILMLARI
movies = {
    "Qasoskorlar-1": {
        "name": "BIRINCHI QASOSKOR / KAPITAN AMERIKA",
        "year": 2011,
        "link": "https://t.me/qasoskorlar_kinol/22"
    },
    "Qasoskorlar-2": {
        "name": "BIRINCHI QASOSKOR 2 / KAPITAN AMERIKA 2",
        "year": 2014,
        "link": "https://t.me/qasoskorlar_kinol/23"
    },
    "Qasoskorlar-3": {
        "name": "BIRINCHI QASOSKOR 3 / KAPITAN AMERIKA 3",
        "year": 2016,
        "link": "https://t.me/qasoskorlar_kinol/24"
    }
}


@dp.message(F.text.in_(movies.keys()))
async def show_movie(message: Message):
    movie = movies[message.text]

    await message.answer(
        f"🎬 Nomi: {movie['name']}\n"
        f"🌏 Mamlakat: AQSH\n"
        f"🎭 Janr: Jangari, Fantastika\n"
        f"📆 Yili: {movie['year']}\n\n"
        f"🎥 {movie['link']}",
        reply_markup=qasos_button
    )


# TRANSFORMERLAR 1
@dp.message(F.text == "Transformerlar 1")
async def transformerlar_1(message: Message):
    await message.answer(
        "🎬 Nomi: Transformerlar 1\n"
        "📆 Yili: 2007\n"
        "🎥 https://t.me/qasoskorlar_kinol/10",
        reply_markup=transformer_button
    )
 # JONUKI 1
@dp.message(F.text == "JonUki 1")
async def jonuki_1(message: Message):
    await message.answer(
        "🎬 Nomi: JonUki 1\n"
        "📆 Yili: 2014\n"
        "🎥 https://t.me/qasoskorlar_kinol/14",
        reply_markup=jonuki_button
    )


# JONUKI 2
@dp.message(F.text == "JonUki 2")
async def jonuki_2(message: Message):
    await message.answer(
        "🎬 Nomi: JonUki 2\n"
        "📆 Yili: 2017\n"
        "🎥 https://t.me/qasoskorlar_kinol/15",
        reply_markup=jonuki_button
    )


# QASOSKORLAR 4
@dp.message(F.text == "Qasoskorlar-4")
async def qasoskorlar_4(message: Message):
    await message.answer(
        "🎬 Bu film tez orada qo'shiladi!",
        reply_markup=qasos_button
    )



# BOSHQA KATEGORIYALAR
@dp.message(F.text.in_(["Ramantik", "Serial", "Ujis"]))
async def categories(message: Message):
    await message.answer(
        "🎬 Bu bo'lim tez orada qo'shiladi!",
        reply_markup=menu
    )


# ORTGA
@dp.message(F.text.in_(["Ortga", "Ortga:"]))
async def back(message: Message):
    await message.answer(
        "🏠 Bosh menyu",
        reply_markup=menu
    )


# BOTNI ISHGA TUSHIRISH
async def main():
    bot = Bot(token=BOT_TOKEN)

    try:
        print("Bot ishga tushdi!")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())











































