import asyncio
import random
import emoji
import aiogram.types
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
TEXT_FILE = 'BQACAgIAAxkBAAOuYe_AiYCct4ioCrT6wW3xo4-5OswAAs4TAAKQiYBLRQJdVfPiIXcjBA'
VIDEO_NOTE = ['DQACAgIAAxkBAAOkYe-WfEm4cWLm9Eke3PphQfFwCccAAiMVAAKQiXhLZGtotoiXS-MjBA',
              'DQACAgIAAxkBAAPlYe_NHDoEFCDTSjVoAAENg5VzwtmoAAJxGwACyj54S8CQp3jxlVZEIwQ']


@dp.message_handler(commands=['start']) #Начало работы
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help']) # Обработка команды /help
async def process_help_command(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды: '), '/voice', '/photo', '/group', '/note', '/file','/testpre', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(commands=['voice']) # Обработка команды /voice
async def process_voice_command(message: types.Message):
    await  bot.send_voice(message.from_user.id, VOICE, reply_to_message_id=message.message_id)

@dp.message_handler(commands=['photo']) # Обработка команды /photo
async def process_photo_command(message: types.Message):
    caption = 'None'
    await bot.send_photo(message.from_user.id, USSR[random.randint(0, len(USSR)-1)], caption=caption, reply_to_message_id=message.message_id)

@dp.message_handler(commands=['group']) # Обработка команды /group
async def process_group_command(message: types.Message):
    media = []
    for i in USSR:
        media.append(InputMediaPhoto(i))

    await bot.send_media_group(message.from_user.id, media)

@dp.message_handler(commands=['note']) # Обработка команды /note
async def process_note_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)
    await asyncio.sleep(1)
    await bot.send_video_note(message.from_user.id, VIDEO_NOTE[random.randint(0,1)])

@dp.message_handler(commands=['file']) # Обработка команды /file
async def process_file_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(1)
    await bot.send_document(user_id,TEXT_FILE,caption='Just a file.')

@dp.message_handler(commands=['testpre']) # Обработка команды /testpre
async def process_testpre_command(message: types.Message):
    message_text = code('''@dp.message_handler(command=['testpre'])
    async def process_test_command(message: types.Message):
    message_text = pre(emojize('Что-то сломалось :smirk:'))
    await bot.send_message(message.from_user.id, message_text)''')
    await bot.send_message(message.from_user.id, message_text, parse_mode = ParseMode.MARKDOWN)

@dp.message_handler() # Обработка любых сообщений
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

@dp.message_handler(content_types=types.ContentType.ANY) # Что-то несвойственное
async def unknow_message(msg: types.Message):
    message_text = text(emoji.emojize('Я не знаю, что с этим делать :water_wave:\n'),
                        italic('Я просто напомню, '), 'что есть ', code('команда'), '/help')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler(content_types=['video_note'])
async def awaiting(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.video_note.file_id)

if __name__ == '__main__':
    executor.start_polling(dp)

