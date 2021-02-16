import asyncio
import time
from collections import deque
from telethon.tl.functions.channels import LeaveChannelRequest
from fridaybot import CMD_HELP, bot
from fridaybot.utils import admin2_cmd, friday_on_cmd


@friday.on(friday_on_cmd("(leave|bye|kickme)$"))
async def leave(e):
    if e.fwd_from:
        return
    if e.is_private:
        await event.edit("`I Can't Do That.`")
        return
    await e.edit(f"My Master {bot.me.first_name} Wishes To Leave This Chat, So Bye.")
    await e.client.kick_participant(e.chat_id, bot.me.id)


@borg.on(admin2_cmd("Loll$"))
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
    if e.fwd_from:
        return
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


@borg.on(admin2_cmd("Hmm$"))
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
    if e.fwd_from:
        return
    t = "Oof"
    for j in range(6):
        t = t[:-1] + "of"
        await e.edit(t)


@friday.on(friday_on_cmd("ccry$"))
async def cry(e):
    if e.fwd_from:
        return
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")


@friday.on(friday_on_cmd("fap$"))
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
CMD_HELP.update({"fap": "Faking orgasm"})
