# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon.tl.types import ChannelParticipantsAdmins

from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"administrator", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Administrators : "
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


@friday.on(friday_on_cmd(pattern="tagall(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    chat = await event.get_input_chat()
    mentions = ""
    sh = event.pattern_match.group(1) if event.pattern_match.group(1) else "Hi !"
    async for x in event.client.iter_participants(chat):
        mentions += f"[{x.first_name}](tg://user?id={x.id}) \n"
    await event.delete()
    n = 4096
    kk = [mentions[i:i+n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"**{sh}** \n{i}"
        await event.client.send_message(event.chat_id, j)


CMD_HELP.update(
    {
        "tagall": "**Tagall**\
\n\n**Syntax : **`.tagall`\
\n**Usage :** tag everyone in a group"
    }
)
