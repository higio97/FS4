# (©) Anonymous

import pyromod.listen
import sys

import pyrogram
from pyrogram import Client
from pyrogram.enums import ParseMode, ChatType

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_1,
    FORCE_SUB_2,
    FORCE_SUB_3,
    FORCE_SUB_4,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
            self.LOGGER(__name__).info(
                f"TG_BOT_TOKEN detected!\nFirst Name: {self.namebot}\nUsername: @{self.username}\n"
            )
            # self.LOGGER(__name__).info(
            #     f"TG_BOT_TOKEN detected!\n┌ First Name: {self.namebot}\n└ Username: @{self.username}\n——"
            # ) # Diwindows eror
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).info(
                "Bot Berhenti."
            )
            print(a)
            sys.exit()

        if FORCE_SUB_1:
            try:
                info = await self.get_chat(FORCE_SUB_1)
                link = info.invite_link
                self.type1 = "ᴄʜᴀɴɴᴇʟ" if info.type == ChatType.CHANNEL else "ɢʀᴏᴜᴘ"
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_1)
                    link = info.invite_link
                self.invitelink1 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_1 detected!\nTitle: {info.title}\nChat ID: {info.id}\n"
                )
                # self.LOGGER(__name__).info(
                #     f"FORCE_SUB_1 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                # ) # Diwindows eror
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_1!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di {self.type1} Tersebut, Chat ID F-Subs Saat Ini: {FORCE_SUB_1}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti."
                )
                sys.exit()

        if FORCE_SUB_2:
            try:
                info = await self.get_chat(FORCE_SUB_2)
                link = info.invite_link
                self.type2 = "ᴄʜᴀɴɴᴇʟ" if info.type == ChatType.CHANNEL else "ɢʀᴏᴜᴘ"
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_2)
                    link = info.invite_link
                self.invitelink2 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_2 detected!\nTitle: {info.title}\nChat ID: {info.id}\n"
                )
                # self.LOGGER(__name__).info(
                #     f"FORCE_SUB_2 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                # ) # Diwindows eror
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_2!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di {self.type2} Tersebut, Chat ID F-Subs Saat Ini: {FORCE_SUB_2}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti."
                )
                sys.exit()

        if FORCE_SUB_3:
            try:
                info = await self.get_chat(FORCE_SUB_3)
                link = info.invite_link
                self.type3 = "ᴄʜᴀɴɴᴇʟ" if info.type == ChatType.CHANNEL else "ɢʀᴏᴜᴘ"
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_3)
                    link = info.invite_link
                self.invitelink3 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_3 detected!\nTitle: {info.title}\nChat ID: {info.id}\n"
                )
                # self.LOGGER(__name__).info(
                #     f"FORCE_SUB_2 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                # ) # Diwindows eror
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_2!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di {self.type3} Tersebut, Chat ID F-Subs Saat Ini: {FORCE_SUB_3}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti."
                )
                sys.exit()

        if FORCE_SUB_4:
            try:
                info = await self.get_chat(FORCE_SUB_4)
                link = info.invite_link
                self.type4 = "ᴄʜᴀɴɴᴇʟ" if info.type == ChatType.CHANNEL else "ɢʀᴏᴜᴘ"
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_4)
                    link = info.invite_link
                self.invitelink4 = link
                self.LOGGER(__name__).info(
                    f"FORCE_SUB_4 detected!\nTitle: {info.title}\nChat ID: {info.id}\n"
                )
                # self.LOGGER(__name__).info(
                #     f"FORCE_SUB_2 detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                # ) # Diwindows eror
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_2!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di {self.type4} Tersebut, Chat ID F-Subs Saat Ini: {FORCE_SUB_4}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti."
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message", disable_notification=True)
            await test.delete()
            self.LOGGER(__name__).info(
                f"CHANNEL_ID Database detected!\nTitle: {db_channel.title}\nChat ID: {db_channel.id}\n"
            )
            # self.LOGGER(__name__).info(
            #     f"CHANNEL_ID Database detected!\n┌ Title: {db_channel.title}\n└ Chat ID: {db_channel.id}\n——"
            # ) # Diwindows eror
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan @{self.username} adalah admin di Channel DataBase anda, CHANNEL_ID Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "Bot Berhenti."
            )
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"[🔥⭐ BERHASIL DIAKTIFKAN! ⭐🔥]\n\nBOT Dibuat oleh @{OWNER}\n\nBot version {pyrogram.__version__}"
        )
        # self.LOGGER(__name__).info(
        #     f"[🔥⭐ BERHASIL DIAKTIFKAN! ⭐🔥]\n\nBOT Dibuat oleh @{OWNER}"
        # ) # Diwindows eror

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
