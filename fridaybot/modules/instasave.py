# created by @Mr_Hops
"""insta save: Avaible commands: .insta <link>
"""


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from fridaybot.utils import admin_cmd


@borg.on(admin_cmd(pattern="instag ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@Regrambot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=274562699)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @Regrambot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)
