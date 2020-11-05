import asyncio

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="dp ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("😎Jaha matter bada hota hai😎")
        await asyncio.sleep(2)
        await event.edit("Eagle DP 😈wahi khada hota hai 💪")
        await asyncio.sleep(2)
        await event.edit("😡Tera baap hu madharchod😒")
        await asyncio.sleep(2)
        await event.edit("😏Naam yad rakhna😏")
        await asyncio.sleep(2)
        await event.edit("😎Tera baap EAGLE DP🤓")
        await asyncio.sleep(2)
        await event.edit("🔥Eagle DP🔥")
        await asyncio.sleep(2)
        await event.edit(
            "😎Jaha matter bada hota hai😎. Eagle DP wahi khada hota hai😏. Tera baap hu madharchod😈. Naam yad rakhna😡. Tera baap EAGLE DP. 🔥🔥🔥🔥🔥"
        )
