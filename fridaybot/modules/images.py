"""Download & Upload Images on Telegram\n
Syntax: `.img <Name>` or `.img (replied message)`
\n Upgraded and Google Image Error Fixed
"""

import os
import shutil
from re import findall

from fridaybot import CMD_HELP
from fridaybot.googol_images import googleimagesdownload
from fridaybot.utils import admin_cmd


@borg.on(admin_cmd(pattern="img ?(.*)"))
async def img_sampler(event):
    await event.edit("`Processing...`")
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        query = reply.message
    else:
        await event.edit("`um, mind mentioning what I actually need to search for ;_;`")
        return

    lim = findall(r"l=\d+", query)
    # lim = event.pattern_match.group(1)
    try:
        lim = lim[0]
        lim = lim.replace("l=", "")
        query = query.replace("l=" + lim[0], "")
    except IndexError:
        lim = 10
    response = googleimagesdownload()

    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }

    # passing the arguments to the function
    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(
        await event.client.get_input_entity(event.chat_id), lst
    )
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()


@borg.on(admin_cmd(pattern="image ?(.*)"))
async def img_sampler(event):
    await event.edit("`Processing...`")
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        query = reply.message
    else:
        await event.edit("`um, mind mentioning what I actually need to search for ;_;`")
        return

    lim = findall(r"l=\d+", query)
    # lim = event.pattern_match.group(1)
    try:
        lim = lim[0]
        lim = lim.replace("l=", "")
        query = query.replace("l=" + lim[0], "")
    except IndexError:
        lim = 10
    response = googleimagesdownload()

    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }

    # passing the arguments to the function
    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(
        await event.client.get_input_entity(event.chat_id), lst
    )
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()


CMD_HELP.update(
    {
        "img": "Syntax: `.img <Name>` or `.img (replied message)` or `.img l=limit <Name>`\
    \nUsage: Download & Upload Images on Telegram using google."
    }
)
