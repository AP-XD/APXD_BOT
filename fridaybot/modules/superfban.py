#  (c)2020 TeleBot
#
# You may not use this plugin without proper authorship and consent from @borgSupport
#

import asyncio

from fridaybot.utils import admin_cmd


# By @HeisenbergTheDanger, @its_xditya
@borg.on(admin_cmd("superfban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Starting a Mass-FedBan...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        FBAN = previous_message.from_id
        REASON = event.pattern_match.group(1)
        if REASON.strip() == "":
            REASON = " #TBMassBanned "
    else:
        arg = event.pattern_match.group(1)
        args = arg.split()
        if len(args) > 1:
            FBAN = args[0]
            REASON = ""
            for a in args[1:]:
                REASON += a + " "
        else:
            FBAN = arg
            REASON = " #TBMassBanned "
    try:
        int(FBAN)
        if int(FBAN) == 630654925 or int(FBAN) == 719195224:
            await event.edit("Something went wrong.")
            return
    except:
        if FBAN == "@HeisenbergTheDanger" or FBAN == "@xditya":
            return
    if Config.FBAN_GROUP_ID:
        chat = Config.FBAN_GROUP_ID
    else:
        chat = await event.get_chat()
    fedList = []
    async with telebot.conversation("@MissRose_bot") as bot_conv:
        await bot_conv.send_message("/start")
        await bot_conv.send_message("/myfeds")
        response = await bot_conv.get_response()
        if "make a file" in response.text:
            await asyncio.sleep(1)
            await response.click(0)
            fedfile = await bot_conv.get_response()
            if fedfile.media:
                downloaded_file_name = await telebot.download_media(fedfile, "fedlist")
                file = open(downloaded_file_name, "r")
                lines = file.readlines()
                for line in lines:
                    fedList.append(line[: line.index(":")])
            else:
                return
        if "You can only use fed commands once every 5 minutes" in response.text:
            await event.edit("Try again after 5 mins.")
            return
        In = False
        tempFedId = ""
        for x in response.text:
            if x == "`":
                if In:
                    In = False
                    fedList.append(tempFedId)
                    tempFedId = ""
                else:
                    In = True

            elif In:
                tempFedId += x

    await event.edit(f"Fbaning in {len(fedList)} feds.")
    try:
        await telebot.send_message(chat, f"/start")
    except:
        await event.edit("FBAN_GROUP_ID is incorrect.")
        return
    await asyncio.sleep(3)
    if Config.EXCLUDE_FED:
        excludeFed = Config.EXCLUDE_FED.split("|")
        for n in range(len(excludeFed)):
            excludeFed[n] = excludeFed[n].strip()
    exCount = 0
    for fed in fedList:
        if Config.EXCLUDE_FED and fed in excludeFed:
            await telebot.send_message(chat, f"{fed} Excluded.")
            exCount += 1
            continue
        await telebot.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(3)
        await telebot.send_message(chat, f"/fban {FBAN} {REASON}")
        await asyncio.sleep(3)
    await event.edit(
        f"SuperFBan Completed. Affected {len(fedList) - exCount} feds.\n#TB"
    )


# By @HeisenbergTheDanger, @its_xditya
@borg.on(admin_cmd("superunfban ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Starting a Mass-UnFedBan...")
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        FBAN = previous_message.from_id
    else:
        FBAN = event.pattern_match.group(1)

    if Config.FBAN_GROUP_ID:
        chat = Config.FBAN_GROUP_ID
    else:
        chat = await event.get_chat()
    fedList = []
    async with telebot.conversation("@MissRose_bot") as bot_conv:
        await bot_conv.send_message("/start")
        await bot_conv.send_message("/myfeds")
        response = await bot_conv.get_response()
        if "make a file" in response.text:
            await asyncio.sleep(1)
            await response.click(0)
            fedfile = await bot_conv.get_response()
            if fedfile.media:
                downloaded_file_name = await telebot.download_media(fedfile, "fedlist")
                file = open(downloaded_file_name, "r")
                lines = file.readlines()
                for line in lines:
                    fedList.append(line[: line.index(":")])
            else:
                return
        if "You can only use fed commands once every 5 minutes" in response.text:
            await event.edit("Try again after 5 mins.")
            return
        In = False
        tempFedId = ""
        for x in response.text:
            if x == "`":
                if In:
                    In = False
                    fedList.append(tempFedId)
                    tempFedId = ""
                else:
                    In = True

            elif In:
                tempFedId += x

    await event.edit(f"UnFbaning in {len(fedList)} feds.")
    try:
        await telebot.send_message(chat, f"/start")
    except:
        await event.edit("FBAN_GROUP_ID is incorrect.")
        return
    await asyncio.sleep(3)
    for fed in fedList:
        await telebot.send_message(chat, f"/joinfed {fed}")
        await asyncio.sleep(3)
        await telebot.send_message(chat, f"/unfban {FBAN}")
        await asyncio.sleep(3)
    await event.edit(f"SuperUnFBan Completed. Affected {len(fedList)} feds.\n#TB")


# By @HeisenbergTheDanger, @its_xditya

"""
.superfban <username/userid> <reason>\
\n**Usage**: Mass-Ban in all feds you are admin in.\
\nSet `EXCLUDE_FED fedid1|fedid2` in heroku vars to exclude those feds.\
\nSet var `FBAN_GROUP_ID` ti the group with rose, where you want FBan to take place.\
\n\nGet help - @borgSupport\
"""
