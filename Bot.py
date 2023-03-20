from aiogram import Bot, Dispatcher, executor, types
import python_weather
import asyncio

# bot input
bot = Bot(token="6094394753:AAFyCPhX_llLWS1i4CTwO1CMx8Iwki8moSM")
dp = Dispatcher(bot)

# echo
@dp.message_handler()
async def echo(message: types.Message):
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        weather = await client.get(message.text)
        celcius = round((weather.current.temperature - 32) / 1.8)
        resp_msg = weather.nearest_area.name + " " + weather.nearest_area.country + '\n'
        resp_msg += f"Текущая температура: {celcius}\n"
        resp_msg += f"Состояние погоды: {weather.current.type}"

    await message.answer(resp_msg)

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    asyncio.run(getweather())