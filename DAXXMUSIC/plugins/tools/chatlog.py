import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID as LOG_GROUP_ID
from DAXXMUSIC import app 
from pyrogram.errors import RPCError
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, aiohttp
from pathlib import Path
from pyrogram.enums import ParseMode

photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(chat.id)
    for member in message.new_chat_members:
        if member.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            msg = (
                f"вσт α∂∂є∂ ηєω gяσυρ\n\n"
                f"____________________________________\n\n"
                f"🪄 ¢нαт-ηαмє: {chat.title}\n"
                f"🍂 ¢нαт-ι∂: {chat.id}\n"
                f"👀 ¢нαт-υѕєяηαмє: @{chat.username}\n"
                f"🔗 ¢нαт-ℓιηк: [тσυ¢н]({link})\n"
                f"🎏 gяσυρ-мємвєяѕ: {count}\n"
                f"🕊 α∂∂є∂-ву: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"¢нє¢к gяσυρ", url=f"{link}")]
            ]))

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "υηкησωη-υѕєя"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "ρяιναтє-¢нαт"
        chat_id = message.chat.id
        left = f"✫ <b><u>#ℓєƒт-gяσυρ</u></b> ✫\n\n¢нαт-тιтℓє : {title}\n\n¢нαт-ι∂ : {chat_id}\n\nкι¢кє∂ ву : {remove_by}\n\nвσт : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
        
