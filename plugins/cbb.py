#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={1808873617}'>CrazyboyOfficial</a>\n○ Made By : <code>CrazyboyOfficial</code>\n○ Copyright : <a href='https://telegram.me/RBMPrime_bot'>Click Here</a>\n○ Any Issue : <a href='https://telegram.me/RBMPrime_Bot'>Click Here</a>\n○ Channel : @CrazyboyOfficial\n○ To Create Your Own Bot Like This Text : @RBMPrime_Bot</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
