import base64
import httpx
import os
import requests 
from pyrogram import filters
from config import BOT_USERNAME
from DAXXMUSIC import app
from pyrogram import filters
import pyrogram
from uuid import uuid4
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


@app.on_message(filters.reply & filters.command("upscale"))
async def upscale_image(app, message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            await message.reply_text("**ρℓєαѕє яєρℓу тσ αη ιмg тσ υρѕ¢αℓє ιт.**")
            return

        image = message.reply_to_message.photo.file_id
        file_path = await app.download_media(image)

        with open(file_path, "rb") as image_file:
            f = image_file.read()

        b = base64.b64encode(f).decode("utf-8")

        async with httpx.AsyncClient() as http_client:
            response = await http_client.post(
                "https://api.qewertyy.me/upscale", data={"image_data": b}, timeout=None
            )

        with open("upscaled.png", "wb") as output_file:
            output_file.write(response.content)

        await client.send_document(
            message.chat.id,
            document="upscaled.png",
            caption="**нєяє ιѕ тнє υρѕ¢αℓє∂ ιмg!**",
        )

    except Exception as e:
        print(f"**ƒαιℓє∂ тσ υρѕ¢αℓє∂ тнє ιмg**: {e}")
        await message.reply_text("**ƒαιℓє∂ тσ υρѕ¢αℓє∂ тнє ιмg. ρℓєαѕє тяу αgαιη**.")


# ------------


waifu_api_url = 'https://api.waifu.im/search'

# Its_Aryaan

def get_waifu_data(tags):
    params = {
        'included_tags': tags,
        'height': '>=2000'
    }

    response = requests.get(waifu_api_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.on_message(filters.command("waifu"))
def waifu_command(client, message):
    try:
        tags = ['maid']  # You can customize the tags as needed
        waifu_data = get_waifu_data(tags)

        if waifu_data and 'images' in waifu_data:
            first_image = waifu_data['images'][0]
            image_url = first_image['url']
            message.reply_photo(image_url)
        else:
            message.reply_text("ησ ωαιƒυ ƒσυη∂ ωιтн тнє ѕρє¢ιƒιє∂ тαgѕ.")

    except Exception as e:
        message.reply_text(f"αη єяяσя σ¢¢υяяє∂: {str(e)}")
