from aiogram import Bot, Dispatcher, executor, types


dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\n"
                        "Я Эхо-бот!\n"
                        "Отправь мне любое сообщение, а я тебе обязательно отвечу.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)