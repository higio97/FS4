# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

import os

from bot import Bot
from pyrogram import Client, filters
from pyrogram.types import Message

from config import ADMINS, LOGGER

@Bot.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply_text("`Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ Bot has restarted !\n\n")
    os.system(f"kill -9 {os.getpid()} && bash start")
