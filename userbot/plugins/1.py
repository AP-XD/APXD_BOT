import aiohttp
import asyncio
import os
import time
from datetime import datetime
from telethon import events
from telethon.tl.types import DocumentAttributeVideo
import json
import subprocess
import math
from pySmartDL import SmartDL
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from userbot import LOGS, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.utils import admin_cmd, humanbytes, progress, time_formatter
from userbot.uniborgConfig import Config
thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"
import io

@borg.on(admin_cmd(pattern="hehe (.*)", outgoing=True))                
async def _(event):
    if event.fwd_from:
        return
    mone = await event.reply("Processing ...")
    input_str = event.pattern_match.group(1)
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    if os.path.exists(input_str):
        start = datetime.now()
        c_time = time.time()
        hmm = await bot.send_file(
            event.chat_id,
            input_str,
            force_document=True,
            supports_streaming=True,
            allow_cache=False,
            reply_to=event.message.id,
            thumb=thumb,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, mone, c_time, "trying to upload")
            )
        )
        end = datetime.now()
        ms = (end - start).seconds
        await mone.delete()
        await hmm.edit("Uploaded in {} seconds.".format(ms))
    else:
        await mone.edit("404: File Not Found")