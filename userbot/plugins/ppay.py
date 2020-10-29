"""Emoji
Available Commands:
.ppay
Credits to @levingod
"""

from telethon import events

import asyncio

from fridaybot.utils import admin_cmd


@borg.on(admin_cmd("ppay"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "levin":
    await event.edit("@levingod")
    animation_chars = [
            "Pay @levingod",
            " Payment method we accept are ",
            "paytm",
            "BTC",
            "Google Pay",
            "Choose your payment method at @paylevin",
            
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
