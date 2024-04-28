import aiohttp
from io import BytesIO
from DAXXMUSIC import app
from pyrogram import filters



async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image



@app.on_message(filters.command("carbon"))
async def _carbon(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("**яєρℓу тσ α тєχт мѕg тσ мαкє α ¢αявση.**")
        return
    if not (replied.text or replied.caption):
        return await message.reply_text("**яєρℓу тσ α тєχт мѕg тσ мαкє α ¢αявση.**")
    text = await message.reply("мαкєιηgg...")
    carbon = await make_carbon(replied.text or replied.caption)
    await text.edit("**ѕєη∂ιηg...**")
    await message.reply_photo(carbon)
    await text.delete()
    carbon.close()


