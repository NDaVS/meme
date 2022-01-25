import random
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

TOKEN = ''

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

MARS = 'AgACAgIAAxkBAAMhYe0vz0eFpO29t2Pv7-M9cpCVmnoAAq-3MRt7_mhLqR8sQsyTYIMBAAMCAANzAAMjBA'
USSR = [
    'AgACAgIAAxkBAANtYe9ARk6yBY5G5qGt5z1vNUw_WzgAAm25MRuQiXhLruC82m5smcgBAAMCAANzAAMjBA',
    'AgACAgIAAxkBAANrYe9ADXgsGAZFQPbxsqEZEzkc3JkAAmy5MRuQiXhLEuVQWemq9eYBAAMCAANzAAMjBA',
    'AgACAgIAAxkBAANpYe8__p-L-xx9eb4Dy6aAfHpzgv8AAmu5MRuQiXhLF8U5BkNoth0BAAMCAANzAAMjBA',
    'AgACAgIAAxkBAANHYe5p2o1Y8PU-chO-tbPMMXFDegsAAqS7MRvcunFLZyWWJf8byRoBAAMCAANzAAMjBA',
    'AgACAgIAAxkBAAMhYe0vz0eFpO29t2Pv7-M9cpCVmnoAAq-3MRt7_mhLqR8sQsyTYIMBAAMCAANzAAMjBA'

]
VOICE = 'AwACAgIAAxkBAAMZYe0tXSLpk-T6zcKkiP8QiisfpbMAAqkTAAJL2mhLPr7VsswlHxAjBA'
VIDEO = 'BAADAgADXAEAAnhu6ErDHE-xNjIzMgI'
TEXT_FILE = 'BQADAgADWgEAAnhu6ErgyjSYkwOL6AI'
VIDEO_NOTE = 'DQADAgADWwEAAnhu6EoFqDa-fStSmgI'

@dp.message_handler(commands=['start']) #Начало работы
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help']) # Обработка команды /help
async def process_help_command(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды: '), '/voice', '/photo', '/group', '/note', '/file','/testpre', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['voice'])
async def process_voice_command(message: types.Message):
    await  bot.send_voice(message.from_user.id, VOICE, reply_to_message_id=message.message_id)

@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    caption = 'None'
    await bot.send_photo(message.from_user.id, USSR[random.randint(0, len(USSR)-1)], caption=caption, reply_to_message_id=message.message_id)

@dp.message_handler(commands=['group'])
async def process_group_command(message: types.Message):
    media = []
    for i in USSR:
        media.append(InputMediaPhoto(i))

    await bot.send_media_group(message.from_user.id, media)

@dp.message_handler(content_types=['photo'])
async def awaiting(message: types.Message):
    DEBAG = True
    if DEBAG:
        await bot.send_message(message.from_user.id, message.photo)



if __name__ == '__main__':
    executor.start_polling(dp)

