import subprocess
import os
from fridaybot.utils import admin_cmd
import glob

@borg.on(admin_cmd("song ?(.*)"))
async def _(event):
    song = url = event.pattern_match.group(1) + " " + "song"
    if not song:
        await event.edit("`Enter song name`")
        return
    await event.edit("Processing...")
    os.system(f"youtube-dl -x --audio-format mp3 --add-metadata --embed-thumbnai 'ytsearch:{song}'")
    l = glob.glob("*.mp3")
    if not l:
        await event.edit("`Song not found`")
        return
    await event.client.send_file(event.chat_id, l, supports_streaming=True, reply_to=event.message)
    await event.delete()
    subprocess.check_output("rm -rf *.mp3",shell=True)