# Credits @buddhhu
# Only for Plus+ UserBot

import asyncio
from datetime import datetime

from fridaybot.utils import admin_cmd


@borg.on(admin_cmd(pattern="boostdl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.reply("Processing...")
    url = event.pattern_match.group(1)
    start = datetime.now()
    cmd = f"aria2c {url}"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    end = datetime.now()
    ms = (end - start).seconds
    await event.reply(f"**Downloaded in {ms} seconds.**\n`Upload using upload plugin.`")
