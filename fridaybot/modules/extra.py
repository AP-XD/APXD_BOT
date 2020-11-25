import asyncio
import time
from collections import deque

from telethon.tl.functions.channels import LeaveChannelRequest

from fridaybot import CMD_HELP, bot
from fridaybot.utils import admin2_cmd, friday_on_cmd


@friday.on(friday_on_cmd("leave$"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I iz Leaving dis Lol Group kek!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`But Boss! This is Not A Chat`")


@borg.on(admin2_cmd("Lol$"))
# @register(outgoing=True, pattern="^;__;$")
async def lolo(e):
    animation_ttl = range(0, 8)
    t = "lol"
    await e.edit(t)
    animation_chars = ["-__-", "-_-"]
    for i in animation_ttl:
        await asyncio.sleep(0.3)
        await e.edit(animation_chars[i % 2])


@borg.on(admin2_cmd("Sed$"))
# @register(outgoing=True, pattern="^;__;$")
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)


@borg.on(admin2_cmd("Yo$"))
# @register(outgoing=True, pattern="^yo$")
async def Ooo(e):
    t = "Yo"
    for j in range(5):
        t = t[:-1] + "oo"
        await e.edit(t)


@borg.on(admin2_cmd("Hmmm$"))
# @register(outgoing=True, pattern="^Hmm$")
async def Mmm(e):
    t = "Hmmm"
    for j in range(5):
        t = t[:-1] + "mm"
        await e.edit(t)


@borg.on(admin2_cmd("Ufff$"))
# @register(outgoing=True, pattern="^Hmm$")
async def UFF(e):
    t = "Ufff"
    for j in range(5):
        t = t[:-1] + "ff"
        await e.edit(t)


@borg.on(admin2_cmd("Fuck$"))
# @register(outgoing=True, pattern="^Hmm$")
async def fck(e):
    t = "Fuck"
    for j in range(8):
        t = t[:-1] + "kk"
        await e.edit(t)


@borg.on(admin2_cmd("Binod$"))
# @register(outgoing=True, pattern="^yo$")
async def Binod(e):
    t = "BINOD"
    for j in range(5):
        t = t[:-1] + "DD"
        await e.edit(t)


@borg.on(admin2_cmd("Oof$"))
# @register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(6):
        t = t[:-1] + "of"
        await e.edit(t)


@friday.on(friday_on_cmd("ccry$"))
# @register(outgoing=True, pattern="^.cry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")


@friday.on(friday_on_cmd("fp$"))
# @register(outgoing=True, pattern="^.fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")


@friday.on(friday_on_cmd("moon$"))
# @register(outgoing=True, pattern="^.mmoon$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(friday_on_cmd("source$"))
# @register(outgoing=True, pattern="^.source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/StarkGang/FridayUserbot")


@friday.on(friday_on_cmd("readme$"))
# @register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("https://github.com/StarkGang/FRIDAYUSERBOT/blob/master/README.md")


@friday.on(friday_on_cmd("heart$"))
# @register(outgoing=True, pattern="^.heart$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@friday.on(friday_on_cmd("fap$"))
# @register(outgoing=True, pattern="^.fap$")
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🍆✊🏻💦"))
    for _ in range(32):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


CMD_HELP.update({"leave": "Leave a Chat"})
CMD_HELP.update({"cry": "Cry"})
CMD_HELP.update({"fp": "Send face palm emoji."})
CMD_HELP.update({"moon": "Bot will send a cool moon animation."})
CMD_HELP.update({"clock": "Bot will send a cool clock animation."})
CMD_HELP.update({"readme": "Reedme."})
CMD_HELP.update({"source": "Gives the source of your fridaybot"})
CMD_HELP.update({"myusernames": "List of Usernames owned by you."})
CMD_HELP.update({"oof": "Same as ;__; but ooof"})
CMD_HELP.update({"earth": "Sends Kensar Earth animation"})
CMD_HELP.update({"heart": "Try and you'll get your emotions back"})
CMD_HELP.update({"fap": "Faking orgasm"})
