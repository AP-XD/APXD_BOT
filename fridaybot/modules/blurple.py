# Made By Sh1vam  Donot KANG
# ME MADE MORE THAN ONE AND MORE COMPLEX ONE WAS YT COMMENT
# I REMOVED COLOUR CAUSE ALL NEED TO REMEMBER HEX COLOUR CODES # replaced by %23
import os

import requests
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto

from fridaybot import bot as borg
from fridaybot.utils import admin_cmd

sedpath = "./shivam/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)

# keep CREDIT LINES ELSE GET LOST


@bot.on(admin_cmd(pattern=r"blur"))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/blur?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(event.chat_id, lolbruh, caption="blur", reply_to=sed)
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)


@bot.on(admin_cmd(pattern=r"blurple "))
async def lolmetrg(event):
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await borg.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await borg.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    url_s = upload_file(img)
    imglink = f"https://telegra.ph{url_s[0]}"
    lolul = f"https://some-random-api.ml/canvas/blurple ?avatar={imglink}"
    r = requests.get(lolul)
    open("shivam.png", "wb").write(r.content)
    lolbruh = "shivam.png"
    await borg.send_file(event.chat_id, lolbruh, caption="blurple ", reply_to=sed)
    for files in (lolbruh, img):
        if files and os.path.exists(files):
            os.remove(files)
