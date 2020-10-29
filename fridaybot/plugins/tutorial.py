"""Plugin to get the video tutorial to deploy TeleBot
.tut"""

from fridaybot.utils import register

@register(outgoing=True, pattern="^.tut$")

async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("Get a fridaybot like mine!! Watch [this video tutorial](https://youtu.be/XmvdDHiIDb4) on deploying...")
