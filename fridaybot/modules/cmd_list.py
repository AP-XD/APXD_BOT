import asyncio
import io
import requests
from fridaybot import CMD_HELP
from fridaybot.utils import friday_on_cmd


# @command(pattern="^.cmds", outgoing=True)
@friday.on(friday_on_cmd(pattern=r"cmds"))
async def install(event):
    if event.fwd_from:
        return
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    cmd = "ls fridaybot/modules"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**List of Plugins:**\n - {o}\n\n**HELP:** __If you want to know the commands for a plugin, do:-__ \n `.help <plugin name>` **without the < > brackets.**\n__All modules might not work directly. Visit__ @FRIDAYSUPPORTOFFICIAL __for assistance.__"
    data = OUTPUT
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": data})
        .json()
        .get("result")
        .get("key")
    )
    url2 = f"https://nekobin.com/{key}"
    raw2 = f"https://nekobin.com/raw/{key}"
    hehe = f"**CMD LIST**.\nPasted to [Nekobin]({url2}) Raw: [View Raw]({raw2}) "    
    if len(OUTPUT) > 4095:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "cmd_list.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=hehe,
                reply_to=reply_to_id,
            )
            await event.delete()
    await event.edit(OUTPUT)


CMD_HELP.update(
    {
        "cmd_list": "**Cmd_list**\
\n\n**Syntax : **`.cmds`\
\n**Usage :** This plugin lists all the plugins which are in your userbot."
    }
)
