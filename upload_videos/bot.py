import asyncio
import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

from config import TOKEN

logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

CAT_BIG_EYES = 'AgADAgADNqkxG3hu6Eov3mINslrI7jUWnA4ABAX7PAfFIfbONj0AAgI'
KITTENS = [
    'AgADAgADN6kxG3hu6EqJjqtjb2_dtnztAw4ABMPliaCdHTFDDxsCAAEC',
    'AgADAgADNakxG3hu6Epaq9GtKVQcmEPqAw4ABKKK02zsSoEJtRwCAAEC',
    'AgADAgADNKkxG3hu6EoNC-hZek5IUkeZQw4ABPbUDtX7JTIZmjwAAgI',
]
VOICE = 'AwADAgADXQEAAnhu6EqAvqdylJRvBgI'
VIDEO = 'BAADAgADXAEAAnhu6ErDHE-xNjIzMgI'
TEXT_FILE = 'BQADAgADWgEAAnhu6ErgyjSYkwOL6AI'
VIDEO_NOTE = 'DQADAgADWwEAAnhu6EoFqDa-fStSmgI'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['note'])
async def process_note_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)
    await asyncio.sleep(1)  # конвертируем видео и отправляем его пользователю
    await bot.send_video_note(message.from_user.id, VIDEO_NOTE)


