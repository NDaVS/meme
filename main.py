# This is a sample Python script.
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

TOKEN = '5165500327:AAHpyjzHY9_-Ys3DihLU3MuFKu2DBU-0-QA'

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

MARS = 'AgACAgIAAxkBAAMhYe0vz0eFpO29t2Pv7-M9cpCVmnoAAq-3MRt7_mhLqR8sQsyTYIMBAAMCAANzAAMjBA'
USSR = [
    'AgACAgIAAxkBAAMvYe0xwHHt56r2ZimifYhp3E59ugMAAr23MRt7_mhLsyGwynPXVq0BAAMCAANzAAMjBA',
    'AgACAgIAAxkBAAMsYe0xlKuhhDPu7cEmL4ZMNaf5oW8AAru3MRt7_mhLjvrdLiU5QLgBAAMCAANzAAMjBA',
    'AgADAgADNKkxG3hu6EoNC-AgACAgIAAxkBAAMqYe0xaNNOz5HMMKdZ1AHa-x1SKIsAAri3MRt7_mhLLnNmtUk2XaIBAAMCAANzAAMjBA',
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
    caption = 'Советская колония на марсе.'
    await bot.send_photo(message.from_user.id, MARS, caption=caption, reply_to_message_id=message.message_id)

@dp.message_handler(commands=['group'])
async def process_group_command(message: types.Message):
    media = []
    for i in USSR:
        media.append(InputMediaPhoto(i))
    print(media)
    await bot.send_media_group(message.from_user.id, media)

@dp.message_handler(content_types=['photo'])
async def awaiting(message: types.Message):
    DEBAG = True
    if DEBAG:
        await bot.send_message(message.from_user.id, message.photo)



if __name__ == '__main__':
    executor.start_polling(dp)

