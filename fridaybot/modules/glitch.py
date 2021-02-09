

import os

from glitch_this import ImageGlitcher
from telethon.tl.types import MessageMediaPhoto
from pygifsicle import optimize
from fridaybot import CMD_HELP
import asyncio
import math
import os
import time
from fridaybot.function import progress, humanbytes, time_formatter
from fridaybot.function.FastTelethon import upload_file
from fridaybot.utils import friday_on_cmd, sudo_cmd
from fridaybot.function import convert_to_image

glitcher = ImageGlitcher()
DURATION = 200  # Set this to however many centiseconds each frame should be visible for
LOOP = 0  # Set this to how many times the gif should loop
# LOOP = 0 means infinite loop

sedpath = "./starkgangz/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)

from fridaybot import CMD_HELP, LOGS
from fridaybot.functions import runcmd, take_screen_shot
from fridaybot.utils import admin_cmd

@borg.on(admin_cmd(pattern="(glitch|glitchs)(?: |$)(.*)"))
@borg.on(admin_cmd(pattern="(glitch|glitchs)(?: |$)(.*)", allow_sudo=True))
async def glitch(cat):
    await cat.reply("`Glitching... 😁`")
    cmd = cat.pattern_match.group(1)
    catinput = cat.pattern_match.group(2)
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.reply("`Media not found...`")
        return
    sed = await event.get_reply_message()
    okbruh = await event.edit("`Gli, Glitchiiingggg.....`")
    photolove = await convert_to_image(event, friday)
    pathsn = f"./starkgangz/@fridayot.gif"
    glitch_imgs = glitcher.glitch_image(photolove, 2, gif=True, color_offset=True)
    glitch_imgs[0].save(
        pathsn,
        format="GIF",
        append_images=glitch_imgs[1:],
        save_all=True,
        duration=DURATION,
        loop=LOOP,
    )
    c_time = time.time()
    optimize(pathsn)
    stark_m = await upload_file(
        	file_name="Glitched@FridayOt.gif",
            client=borg,
            file=open(pathsn, 'rb'),
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, event, c_time, "Uploading..", pathsn
                )
            ),
        )
    await borg.send_file(event.chat_id,
                         stark_m,
                         caption="Powered By @FridayOT")
    await okbruh.delete()
    for starky in (pathsn, photolove):
        if starky and os.path.exists(starky):
            os.remove(starky)


CMD_HELP.update(
    {
        "glitch": "**SYNTAX : **`.glitch` reply to media file\
    \n**USAGE :** glitches the given mediafile(gif , stickers , image, videos) to a gif and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    \n\n**SYNTAX : **`.glitchs` reply to media file\
    \n**USAGE :** glitches the given mediafile(gif , stickers , image, videos) to a sticker and glitch range is from 1 to 8.\
    If nothing is mentioned then by default it is 2\
    "
    }
)
