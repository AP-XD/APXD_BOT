import os
from pathlib import Path

from telethon.tl.types import InputMessagesFilterDocument

from fridaybot.utils import command, load_module
from fridaybot.Configs import Config


@command(pattern="^.extload", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    chat = Var.PLUGIN_CHANNEL
    documentss = await borg.get_messages(chat, None, filter=InputMessagesFilterDocument)
    total = int(documentss.total)
    total_doxx = range(0, total)
    await event.delete()
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await event.client.download_media(
            await borg.get_messages(chat, ids=mxo), "fridaybot/modules/"
        )
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            await borg.send_message(
                event.chat_id,
                "This Plugin `{}` have been Loaded successfully.".format(
                    os.path.basename(downloaded_file_name)
                ),
            )
        else:
            await borg.send_message(
                event.chat_id,
                "Plugin `{}` has been already Loaded and cannot be installed.".format(
                    os.path.basename(downloaded_file_name)
                ),
            )
