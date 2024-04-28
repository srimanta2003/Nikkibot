from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import OWNER_ID as owner_id
from DAXXMUSIC import app



def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@app.on_message(filters.command("bug"))
async def bugs(_, msg: Message):
    if msg.chat.username:
        chat_username = f"@{msg.chat.username}/`{msg.chat.id}`"
    else:
        chat_username = f"ρяιναтє gяσυρ/`{msg.chat.id}`"

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = (
        "[" + msg.from_user.first_name + "](tg://user?id=" + str(msg.from_user.id) + ")"
    )
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    

    bug_report = f"""
**#вυg : ** **tg://user?id={owner_id}**

**яєρσятє∂ ву : ** **{mention}**
**υι∂ : ** **{user_id}**
**¢нαт-ℓιηк : ** **{chat_username}**

**вυg : ** **{bugs}**

**єνєηт ѕтαмρ : ** **{datetimes}**"""

    if msg.chat.type == "private":
        await msg.reply_text("<b>» тнιѕ σηℓу ƒσя gяσυρѕ.</b>")
        return

    if user_id == owner_id:
        if bugs:
            await msg.reply_text(
                "<b>» вσт σωηєя нσ ααρ мυʝнѕє мαʝαк мαт кαяσ 🕊.</b>",
            )
            return
        else:
            await msg.reply_text("<b>» вσт σωηєя нσ ααρ мυʝнѕє мαʝαк мαт кαяσ 🕊.</b>")
    elif user_id != owner_id:
        if bugs:
            await msg.reply_text(
                f"<b>вυg яєρσят : {bugs}</b>\n\n"
                "<b>» ѕυ¢¢єѕѕƒυℓ Яєρσятє∂ </b>",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("⌯ ¢ℓσѕє ⌯", callback_data="close_data")]]
                ),
            )
            await app.send_photo(
                -1002133369721,
                photo="https://telegra.ph/file/1949480f01355b4e87d26.jpg",
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("⌯ νιєω вυg ⌯", url=f"{msg.link}")],
                        [
                            InlineKeyboardButton(
                                "⌯ ¢ℓσѕє ⌯", callback_data="close_send_photo"
                            )
                        ],
                    ]
                ),
            )
        else:
            await msg.reply_text(
                f"<b>» ησ вυg яєρσятѕ !</b>",
            )




@app.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(_,  query :CallbackQuery):
    is_admin = await app.get_chat_member(query.message.chat.id, query.from_user.id)
    if not is_admin.privileges.can_delete_messages:
        await query.answer("уσυ ∂ση'т нανє яιgнтѕ тσ ¢ℓσѕє тнιѕ.", show_alert=True)
    else:
        await query.message.delete()


