# Ported from userge by @buddhhu

import asyncio
import os
import urllib

import requests
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"boobs"))
async def boobs(event):
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("`Finding some big bobs 🧐...`")
    await asyncio.sleep(0.5)
    await a.edit("`Sending some big bobs 🌚...`")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


@borg.on(admin_cmd(pattern=r"butts"))
async def butts(event):
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "butts.jpg")
    a = await event.reply("`Finding some beautiful butts 🧐...`")
    await asyncio.sleep(0.5)
    await a.edit("`Sending some beautiful butts 🌚...`")
    nsfw = requests.get("http://api.obutts.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os

import requests
from telethon.tl.types import MessageMediaPhoto

from fridaybot.utils import friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern=r"nsfw2"))
@friday.on(sudo_cmd(pattern=r"nsfw", allow_sudo=True))
async def nsfw(event):
    url = "https://nsfw-categorize.it/api/upload"
    await event.edit("`Processing..`")
    sed = await event.get_reply_message()
    photo = None
    if replymsg and replymsg.media:
        if isinstance(sed.media, MessageMediaPhoto):
            photo = await borg.download_media(sed.media, sedpath)
        elif "image" in response.media.document.mime_type.split("/"):
            photo = await borg.download_media(sed.media, sedpath)
        else:
            await event.edit("Reply To Image")
            return
    if photo:
        files = {"image": (f"{photo}", open(f"{photo}", "rb"))}
        r = requests.post(url, files=files).json()
        if r["status"] == "OK":
            await event.edit(
                "This image is classified as " + str(r["data"]["classification"])
            )
        if os.path.exists(photo):
            os.remove(photo)
        else:
            await event.edit("Response UnsucessFull. Try Again.")
            if os.path.exists(photo):
                os.remove(photo)
