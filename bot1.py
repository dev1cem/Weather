import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import executor

API_TOKEN = '6134476088:AAFOw3CxvVnPDQ7tlTIdWzF0tP9gJA80x5M'  # Замените на ваш токен API

# Инициализируем бота и диспетчер
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Включаем логирование, чтобы видеть информацию об ошибках
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['weather'])
async def send_weather(message: types.Message):
    """
    Обработчик команды /weather
    """
    city = message.text.split('/weather ', 1)[1]
    weather_api_key = 'e933d79ccf6945638d2212123230906'  # Замените на ваш ключ API погоды

    # Получаем данные о погоде
    response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}')
    data = response.json()

    # Извлекаем нужные данные
    location = data['location']['name']
    condition = data['current']['condition']['text']
    temperature = data['current']['temp_c']

    # Формируем сообщение о погоде
    weather_message = f"Погода в {location}:\nСостояние: {condition}\nТемпература: {temperature}°C"

    await message.answer(weather_message)

if __name__ == '__main__':
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)
