"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @WhySooSerious

import asyncio
from telethon import events
from uniborg.util import admin_cmd, sudo_cmd, edit_or_reply
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/1959ecf64cbca739ef584.png"
pm_caption = "`FRIDAY IS:` **ONLINE**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **1.15.0**\n`Python:` **3.7.4**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `Master`\n"
pm_caption += "**Friday OS** : `3.0`\n"
pm_caption += "**Current Sat** : `丂𝙋⚡️ㄕ𝙄𝙆𝘼𝘾𝙃𝙐𒁂ᴾᴿᴼ𒋨ᵛᶰᴳᵒᵈシ2.25`\n"
pm_caption += f"**My Peru Owner** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "**License** : [GNU General Public License v3.0](github.com/SP-PIKACHU/FridayUserbot/blob/master/LICENSE)\n"
pm_caption += "Copyright : By [SP-PIKACHU@Github](github.com/SP-PIKACHU/FridayUserbot)\n"
pm_caption += "**OS** : `Slim Buster`"
pm_caption += " [Deploy FridayUserbot](https://telegra.ph/file/1959ecf64cbca739ef584.png)"

@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
