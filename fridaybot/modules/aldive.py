# Thanks to Sipak bro and Aryan..
# animation Idea by @(ItzSipak) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import os
from io import BytesIO
import time
import requests
from telethon import events, version           
from PIL import Image
import random
from fridaybot import ALIVE_NAME, Lastupdate
from datetime import datetime                             
from telethon.tl.types import ChannelParticipantsAdmins             
from fridaybot.utils import admin_cmd, sudo_cmd

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

# Thanks to Sipak bro and Raganork..
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/6aa39732748ed7c319943.jpg"
file2 = "https://telegra.ph/file/a6d72504bc09e71484a54.jpg"
file3 = "https://telegra.ph/file/3cdbede1d5d85aa2d50fc.jpg"
file4 = "https://telegra.ph/file/3dae01973943e8b28c931.jpg"
file5 = "https://telegra.ph/file/1c4df5d90d6e68e417348.png"
file6 = "https://telegra.ph/file/37a375d57dcfc5f609980.jpg"
file7 = "https://telegra.ph/file/1ca5834fafa60dc8a817c.png"
""" =======================CONSTANTS====================== """
@borg.on(admin_cmd(pattern=r"aldive"))
@borg.on(sudo_cmd(pattern=r"aldive", allow_sudo=True))
async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = get_readable_time((time.time() - Lastupdate))
    pm_caption = "** 𝙳𝙰𝚁𝙺 𝙲𝙾𝙱𝚁𝙰 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n\n"
    pm_caption += "**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
    pm_caption += "✘ About My System ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ {version.__version__}\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/Dark_cobra_support)\n"
    pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [𝚃𝙴𝙰𝙼 𝙲𝙾𝙱𝚁𝙰](https://github.com/DARK-COBRA)\n"
    pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [𝙳𝙰𝚁𝙺-𝙲𝙾𝙱𝚁𝙰](https://github.com/DARK-COBRA/DARKCOBRA)\n\n"
    pm_caption += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ {uptime}\n\n"
    pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file4)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file7)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file3)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file6)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file5)
