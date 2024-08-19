from aiogram import Router, Bot
from aiogram.types import Message

from bot.data.config import TOKEN_TG
from bot.keyboards.user_keyboards import get_links

router = Router()
bot = Bot(TOKEN_TG)

# this can be retrieved from the database
# RU: это можно доставать из БД
groups = [
    ("василий", "https://t.me/CreateTrigger"),
    ("example", "https://t.me/memchild")
          ]


@router.message()
async def general(message: Message):
    """Eating all messages"""
    if message.chat.type == "private":
        print(message)
        tg_id = message.from_user.id

        links = []

        for group in groups:
            result = await bot.get_chat_member(chat_id=f"@{group[1][13:]}", user_id=tg_id)
            # if you have links to channels without https:... - remove [13:]
            # RU: если у вас ссылки на каналы без https:... - уберите [13:]
            if result.status == "left":
                links.append(group)

        if len(links) > 0:
            await message.answer("Subscribe to the channels:", reply_markup=await get_links(links))
        else:
            await message.answer("You did well!")