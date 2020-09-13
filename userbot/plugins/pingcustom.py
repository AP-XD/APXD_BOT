from telethon import events
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from datetime import datetime

@borg.on(admin_cmd(pattern="piing$"))
@borg.on(sudo_cmd(pattern="piing$", allow_sudo=True))
async def _(event):
    starkislub = await edit_or_reply(event, "`Pong !`")
    if event.fwd_from:
        return
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000    
    await starkislub.edit("**⛔PONG!!⛔**".format(ms))
