import asyncio
import os
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

FONT_FILE_TO_USE = "Fonts/digital.ttf"


@command(pattern="^.seconddp", outgoing=True)
# @borg.on(admin_cmd(pattern=r"seconddp"))
async def seconddp(event):
    downloaded_file_name = "fridaybot/original_pic.png"
    downloader = SmartDL(
        Config.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False
    )
    downloader.start(blocking=False)
    photo = "fridaybot/photo_pfp.png"
    while not downloader.isFinished():
        pass
    counter = -30
    while True:
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        file_test = im.rotate(counter, expand=False).save(photo, "PNG")
        current_time = datetime.now().strftime("%H:%M:%s")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 50)
        drawn_text.text((250, 250), current_time, font=fnt, fill=(124, 252, 0))
        img.save(photo)
        file = await bot.upload_file(photo)  # pylint:disable=E0602
        try:
            await bot(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)
            counter -= 30
            await asyncio.sleep(10)
        except:
            return
