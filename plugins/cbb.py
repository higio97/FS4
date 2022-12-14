# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from bot import Bot
from config import OWNER
from Data import Data
from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, Message


@Bot.on_message(filters.private & filters.incoming & filters.command("about"))
async def _about(client: Bot, msg: Message):
    await client.send_message(
        msg.chat.id,
        Data.ABOUT.format(client.username, OWNER),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.mbuttons),
    )


@Bot.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(client: Bot, msg: Message):
    await client.send_message(
        msg.chat.id,
        "<b>Cara Menggunakan Bot ini</b>\n" + Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )

@Bot.on_message(filters.command("id"))
async def showid(client, message: Message):
    chat_type = message.chat.type.value

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(
            f"<b>User ID anda adalah:</b> <code>{user_id}</code>", quote=True
        )

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += f"<b>👥 Chat ID</b>: <code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += f"<b>🙋‍♂️ Replied User ID</b>: <code>{message.reply_to_message.from_user.id}</code>\n"
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += f"<b>👤 User ID</b>: <code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id, quote=True)


def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker",
        ):
            if obj := getattr(msg, message_type):
                setattr(obj, "message_type", message_type)
                return obj


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        try:
            await query.message.edit_text(
                text=Data.ABOUT.format(client.username, OWNER),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.mbuttons),
            )
        except MessageNotModified:
            pass
    elif data == "help":
        try:
            await query.message.edit_text(
                text="<b>Cara Menggunakan Bot ini</b>\n" + Data.HELP,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.buttons),
            )
        except MessageNotModified:
            pass
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
