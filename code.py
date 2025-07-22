import asyncio
from aiogram import Bot, Dispatcher, types 
from aiogram.filters import CommandStart

bot = Bot(token='')
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Это была команда старт")

@dp.message()
async def echo(message: types.Message):
    text = message.text 
    if text in ['Привет', "привет", 'hi', 'hello']:
        await message.answer('и тебе привет!')
    elif text in ['Пока', 'До свидания', 'ББ']:
        await message.answer('и тебе пока друг!')
    elif text in ['нпп', 'негры пидорасы поголовно']:
        await message.answer('я с тобой полностью согласен!!!')
    else: 
        await message.answer(message.text)






async def main():
    await dp.start_polling(bot)

asyncio.run(main())
