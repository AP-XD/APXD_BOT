# Usage : .spidermandp
# Plugin Moded By @Anonymous_Machinee @AP_XD #
import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from fridaybot.utils import friday_on_cmd

COLLECTION_STRING = [
    "pictures-of-ironman-wallpapers",
    "ironman-hd-wallpaper-1920x1080",
    "ironman-logo-wallpaper",
    "ironman-phone-wallpaper",
    "ironman-3-wallpaper",
    "iron-man-wallpaper-1920x1080",
    "iron-man-wallpapers",
    "hd-spiderman-logo-wallpaper",
    "pictures-of-spiderman-wallpapers",
    "4k-spiderman-wallpaper",
    "spiderman-hd-wallpaper-1920x1080",
    "spiderman-logo-wallpaper",
    "amazing-spiderman-phone-wallpaper",
    "spiderman-3-wallpaper",
]


async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get(
        "http://getwallpapers.com/collection/4k-ironman-wallpaper" + pack
    ).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@friday.on(friday_on_cmd(pattern="spirondp ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Spiderman+IRON MAN's  Profile Pic...\n\nDone ! Check Your DP **"
    )

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(100)  # Edit this to your required needs
