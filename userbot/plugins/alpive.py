import os, time
from .. import ALIVE_NAME, UpTime
from ..utils import get_readable_time as grt
from platform import python_version
from . import UP
from telethon import version
import fridaybot.utils
from uniborg.util import admin_cmd, sudo_cmd
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet."
ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
PLUSPIC = ALIVE_PIC

@borg.on(admin_cmd(pattern="alpive$"))
async def iamalive(alive):
    if alive.fwd_from:
        return
    uptime = grt((time.time() - UpTime))
    if PLUSPIC:
     ALIVE = f"**MADE IN 🇮🇳 , MADE WITH 😍** \n\n`🔸 Telethon :` **{version.__version__}** \n`🔹 Python:` **{python_version()}** \n`🔸 Plus+ Uptime:` **{uptime}** \n`🔹 Plus+ Version:` {UP} \n`🔸 My owner:` **{DEFAULTUSER}**  \n`🔹 Join` @plusub `For Help` \n\n                      [Deploy✔️](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FPlus&template=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FPlus)  \n\n   "
     await alive.client.send_file(alive.chat_id, PLUSPIC, caption=ALIVE, link_preview=False)
     await alive.delete()
    else:
     ALIVE = f"**MADE IN 🇮🇳 , MADE WITH 😍** \n\n`🔸 Telethon :` **{version.__version__}** \n`🔹 Python:` **{python_version()}** \n`🔸 Plus+ Uptime:` **{uptime}** \n`🔹 Plus+ Version:` {UP} \n`🔸 My owner:` **{DEFAULTUSER}**  \n`🔹 Join` @plusub `For Help` \n\n                      [Deploy✔️](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FPlus&template=https%3A%2F%2Fgithub.com%2Famitsharma123234%2FPlus)  \n\n   "
     await alive.send_message(alive.chat_id, ALIVE, link_preview=False)
     await event.delete()