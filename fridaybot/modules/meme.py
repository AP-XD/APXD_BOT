"""
Memes Plugin for Userbot
usage = .meme someCharacter //default delay will be 3
By : - @Zero_cool7870

"""
import asyncio

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"meme"))
async def meme(event):
    if event.fwd_from:
        return
    memeConfig = event.text
    sleepValue = 3
    memeConfig = memeConfig[6:]

    await event.edit("-------------" + memeConfig)
    await asyncio.sleep(sleepValue)
    await event.edit("------------" + memeConfig + "-")
    await asyncio.sleep(sleepValue)
    await event.edit("-----------" + memeConfig + "--")
    await asyncio.sleep(sleepValue)
    await event.edit("----------" + memeConfig + "---")
    await asyncio.sleep(sleepValue)
    await event.edit("---------" + memeConfig + "----")
    await asyncio.sleep(sleepValue)
    await event.edit("--------" + memeConfig + "-----")
    await asyncio.sleep(sleepValue)
    await event.edit("-------" + memeConfig + "------")
    await asyncio.sleep(sleepValue)
    await event.edit("------" + memeConfig + "-------")
    await asyncio.sleep(sleepValue)
    await event.edit("-----" + memeConfig + "--------")
    await asyncio.sleep(sleepValue)
    await event.edit("----" + memeConfig + "---------")
    await asyncio.sleep(sleepValue)
    await event.edit("---" + memeConfig + "----------")
    await asyncio.sleep(sleepValue)
    await event.edit("--" + memeConfig + "-----------")
    await asyncio.sleep(sleepValue)
    await event.edit("-" + memeConfig + "------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeConfig + "-------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeConfig)
    await asyncio.sleep(sleepValue)


"""
Bonus : Flower Boquee Generater
usage:- .flower

"""


@borg.on(admin_cmd(pattern=r"flower"))
async def meme(event):
    if event.fwd_from:
        return
    flower = " 🌹"
    sleepValue = 5

    await event.edit(flower + "        ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower + flower + "       ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower + flower + flower + "      ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower + flower + flower + flower + "     ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower + flower + flower + flower + flower + "    ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower + flower + flower + flower + flower + flower + "   ")
    await asyncio.sleep(sleepValue)
    await event.edit(
        flower + flower + flower + flower + flower + flower + flower + "   "
    )
    await asyncio.sleep(sleepValue)
    await event.edit(
        flower + flower + flower + flower + flower + flower + flower + flower + "  "
    )
    await asyncio.sleep(sleepValue)
    await event.edit(
        flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + " "
    )
    await asyncio.sleep(sleepValue)
    await event.edit(
        flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
        + flower
    )
    await asyncio.sleep(sleepValue)
