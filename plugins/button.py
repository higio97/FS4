# (©) Anonymous

from config import (
    FORCE_SUB_1,
    FORCE_SUB_2,
    FORCE_SUB_3,
    FORCE_SUB_4
)
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_1 and not FORCE_SUB_2 and not FORCE_SUB_3 and not FORCE_SUB_4: # JIKA SEMUA ID TIDAK DIISI
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_2 and not FORCE_SUB_3 and not FORCE_SUB_4 and FORCE_SUB_1: 
        buttons = [
            [
                InlineKeyboardButton(text=f"{client.type1} 𝟷", url=client.invitelink1),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_1 and not FORCE_SUB_3 and not FORCE_SUB_4 and FORCE_SUB_2: 
        buttons = [
            [
                InlineKeyboardButton(text=f"{client.type2} 𝟷", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_1 and not FORCE_SUB_2 and not FORCE_SUB_4 and FORCE_SUB_3:
        buttons = [
            [
                InlineKeyboardButton(text=f"{client.type3} 𝟷", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_1 and not FORCE_SUB_2 and not FORCE_SUB_3 and FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text=f"{client.type4} 𝟷", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_2 and not FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text=f"{client.type1} 𝟷", url=client.invitelink1),
                InlineKeyboardButton(text=f"{client.type2} 2", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_3 and not FORCE_SUB_2 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text=f"{client.type1} 𝟷", url=client.invitelink1),
                InlineKeyboardButton(text=f"{client.type3} 2", url=client.invitelink3),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_4 and not FORCE_SUB_2 and not FORCE_SUB_3:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text=f"{client.type1} 𝟷", url=client.invitelink1),
                InlineKeyboardButton(text=f"{client.type4} 2", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_2 and FORCE_SUB_3 and not FORCE_SUB_1 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text=f"{client.type2} 𝟷", url=client.invitelink2),
                InlineKeyboardButton(text=f"{client.type3} 2", url=client.invitelink3),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_2 and FORCE_SUB_4 and not FORCE_SUB_1 and not FORCE_SUB_3:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text=f"{client.type2} 𝟷", url=client.invitelink2),
                InlineKeyboardButton(text=f"{client.type4} 2", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_3 and FORCE_SUB_4 and not FORCE_SUB_1 and not FORCE_SUB_2:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text=f"{client.type3} 𝟷", url=client.invitelink3),
                InlineKeyboardButton(text=f"{client.type4} 2", url=client.invitelink4),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons
    # batas 2 tombol
    if FORCE_SUB_1 and FORCE_SUB_2 and FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text=f"{client.type1} 𝟷", url=client.invitelink1), 
                InlineKeyboardButton(text=f"{client.type2} 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text=f"{client.type3} 3", url=client.invitelink3)
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_2 and FORCE_SUB_4 and not FORCE_SUB_3:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text=f"{client.type1} 𝟷", url=client.invitelink1),
                InlineKeyboardButton(text=f"{client.type2} 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text=f"{client.type4} 3", url=client.invitelink4)
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_3 and FORCE_SUB_4 and not FORCE_SUB_2:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text=f"{client.type1} 1", url=client.invitelink1),
                InlineKeyboardButton(text=f"{client.type3} 2", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text=f"{client.type4} 3", url=client.invitelink4)
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_2 and FORCE_SUB_3 and FORCE_SUB_4 and not FORCE_SUB_1:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text=f"{client.type2} 1", url=client.invitelink2),
                InlineKeyboardButton(text=f"{client.type3} 2", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text=f"{client.type4} 3", url=client.invitelink4)
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_2 and FORCE_SUB_3 and FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text=f"{client.type1} 1", url=client.invitelink1),
                InlineKeyboardButton(text=f"{client.type2} 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text=f"{client.type3} 3", url=client.invitelink3),
                InlineKeyboardButton(text=f"{client.type4} 4", url=client.invitelink4)
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons

def fsub_button(client, message):
    if FORCE_SUB_1 and not FORCE_SUB_2 and not FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink1),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_2 and not FORCE_SUB_1 and not FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_3 and not FORCE_SUB_1 and not FORCE_SUB_2 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_4 and not FORCE_SUB_1 and not FORCE_SUB_2 and not FORCE_SUB_3:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    
    if FORCE_SUB_1 and FORCE_SUB_2 and not FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink1),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_3 and not FORCE_SUB_2 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink1),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_4 and not FORCE_SUB_2 and not FORCE_SUB_3:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink1),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_2 and FORCE_SUB_3 and not FORCE_SUB_1 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink2),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_2 and FORCE_SUB_4 and not FORCE_SUB_1 and not FORCE_SUB_3:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink2),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_3 and FORCE_SUB_4 and not FORCE_SUB_1 and not FORCE_SUB_2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_2 and FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink1),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 3", url=client.invitelink3)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_2 and FORCE_SUB_4 and not FORCE_SUB_3:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink1),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 3", url=client.invitelink4)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_3 and FORCE_SUB_4 and not FORCE_SUB_2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink1),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 3", url=client.invitelink4)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_2 and FORCE_SUB_3 and FORCE_SUB_4 and not FORCE_SUB_1:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink2),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 3", url=client.invitelink4)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_1 and FORCE_SUB_3 and FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 1", url=client.invitelink1),
                InlineKeyboardButton(text="ᴊᴏɪɴ 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ 3", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ 3", url=client.invitelink4)
            ]
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
