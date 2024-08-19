from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_links(links):

    all_links = []

    for link in links:
        item = InlineKeyboardButton(text=link[0], url=link[1])
        all_links.append(item)

    key = [[button] for button in all_links]
    key = InlineKeyboardMarkup(inline_keyboard=key)

    return key
