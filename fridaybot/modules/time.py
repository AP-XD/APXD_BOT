""" It does not do to dwell on dreams and forget to live
Syntax: .getime"""

import asyncio
import os
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
import pytz 
from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd

FONT_FILE_TO_USE = "Fonts/DroidSansMono.ttf"

IST = pytz.timezone(Config.TZ) 

@friday.on(friday_on_cmd("time$"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    TZ = pytz.timezone(Config.TZ)
    current_time = datetime.now(TZ).strftime(
        f"Time Zone : {Config.TZ} \n\nDate : %Y/%m/%d \nTime : %H:%M:%S"
    )
    start = datetime.now()
    reply_msg_id = event.message.id
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    required_file_name = (
        Config.TMP_DOWNLOAD_DIRECTORY + " " + str(datetime.now()) + ".webp"
    )
    img = Image.new("RGBA", (350, 220), color=(0, 0, 0, 115))
    fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
    drawn_text = ImageDraw.Draw(img)
    drawn_text.text((10, 10), current_time, font=fnt, fill=(255, 255, 255))
    img.save(required_file_name)
    await borg.send_file(  
        event.chat_id,
        required_file_name,
        reply_to=reply_msg_id,
    )
    os.remove(required_file_name)
    end = datetime.now()
    time_taken_ms = (end - start).seconds
    await event.edit("Created sticker in {} seconds".format(time_taken_ms))
    await asyncio.sleep(5)
    await event.delete()

    
@friday.on(friday_on_cmd("(ctime|timenow)$"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    TZ = pytz.timezone(Config.TZ)
    datetime_tz = datetime.now(TZ)
    oof = datetime_tz.strftime(f"**Time Zone :** `{Config.TZ}` \n\n**Date :** `%Y/%m/%d` \n**Time :** `%H:%M:%S`")
    await event.edit(oof)

CMD_HELP.update(
    {
        "time": "**Time**\
\n\n**Syntax : **`.time`\
\n**Usage :** Creates a sticker with present time and date."
    }
)
