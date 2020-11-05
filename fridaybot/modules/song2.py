# Credits @Itzsjdude
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved

import asyncio

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="find (.*)"))
async def _(event):
    chat = "@songdl_Bot"
    input_str = str(event.text[6:])
    chut = await event.reply(f"**Searching for** `{input_str}`")
    async with event.client.conversation(chat) as bot_conv:
        await event.client.send_message(chat, input_str)
        await asyncio.sleep(10)
        reply = await event.client.get_messages(chat)
        if "Pick" in reply[0].message:
            await chut.edit("**Sending Your requested song...**")
            await reply[0].click(0)
            await asyncio.sleep(3)
            a = await event.client.get_messages(chat)
            ac = a[0]
            await event.client.send_file(
                event.chat_id, ac, caption=f"**{input_str}\nUploaded by FRIDAY**"
            )
            await chut.delete()
        else:
            return await chut.edit("**Failed to get your song...**")
