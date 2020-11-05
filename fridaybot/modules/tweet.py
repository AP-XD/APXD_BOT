# By @kirito6969 for PepeBot
# Don't edit credits Madafaka
"""Commands:\n
`.dtrump`
`.imodi`
`.kanna`
`.mind`
`.tweet`
`.carry`"""
import re
from asyncio import sleep

import requests
from global_variables import MODULE
from PIL import Image
from uniborg.util import admin_cmd

MODULE.append("tweet")

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, "", inputString)


@borg.on(admin_cmd(pattern="trump ?(.*)"))
async def trumptweet(event):
    args = event.pattern_match.group(1)
    if not args and not event.reply_to_msg_id:
        a = await event.reply("`Give some text to Doland Trump`")
        await sleep(3)
        await event.delete()
        await a.delete()
        return
    if not args:
        rep = await event.get_reply_message()
        args = rep.text
    b = await event.reply("`Trump Tweeting...`")
    args = deEmojify(args)
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={args}"
    ).json()
    meow = r.get("message")
    if not meow:
        return await b.edit("`Trump not found. He ran away :)`")
    await event.client.send_file(
        event.chat_id, file=meow, reply_to=event.reply_to_msg_id
    )
    await sleep(2)
    await event.delete()
    await b.delete()


@borg.on(admin_cmd(pattern="mind ?(.*)"))
async def changemymind(e):
    args = e.pattern_match.group(1)
    if not args and not e.reply_to_msg_id:
        await e.reply("`Give some text to change_your_min`")
        await sleep(3)
        await e.delete()
        return
    if not args:
        rep = await e.get_reply_message()
        args = rep.text
    a = await e.edit("`Creating Banner...`")
    args = deEmojify(args)
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=changemymind&text={args}"
    ).json()
    wew = r.get("message")
    if not wew:
        return await e.edit("`Can't able to change Mind :(`")
    await e.client.send_file(e.chat_id, file=wew, reply_to=e.reply_to_msg_id)
    await sleep(2)
    await e.delete()
    await a.delete()


@borg.on(admin_cmd(pattern="kanna ?(.*)"))
async def kannagen(e):
    args = e.pattern_match.group(1)
    if not args and not e.reply_to_msg_id:
        await e.reply("`Give some text to Kanna`")
        await sleep(5)
        await e.delete()
        return
    if not args:
        rep = await e.get_reply_message()
        args = rep.text
    args = deEmojify(args)
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=kannagen&text={args}"
    ).json()
    kk = r.get("message")
    if not kk:
        return await e.edit("`Nothing found from the API`")
    a = await e.reply("`Kanna is writing your text`")
    await e.client.send_file(e.chat_id, file=kk, reply_to=e.reply_to_msg_id)
    await sleep(2)
    await e.delete()
    await a.delete()


@borg.on(admin_cmd(pattern="modi ?(.*)"))
async def trumptweet(event):
    args = event.pattern_match.group(1)
    if not args and not event.reply_to_msg_id:
        await event.reply("`Give some text to Modi Bish!`")
        await sleep(5)
        await event.delete()
        return
    if not args:
        replied = await event.get_reply_message()
        args = replied.text
    args = deEmojify(args)
    k = f"https://nekobot.xyz/api/imagegen?type=tweet&text={args}&username=narendramodi"
    r = requests.get(k).json()
    meow = r.get("message")
    if not meow:
        return await event.edit("`Modi not found. He ran away :)`")
    a = await event.reply("`Modi is Tweeting`")
    await event.client.send_file(
        event.chat_id, file=meow, reply_to=event.reply_to_msg_id
    )
    await sleep(2)
    await event.delete()
    await a.delete()


@borg.on(admin_cmd(pattern="tweet ?(.*)"))
async def nekobot(cat):
    kk = cat.pattern_match.group(1)
    replied = await cat.get_reply_message()
    query = kk
    if replied:
        text = replied.message
        username = query
    elif "|" in query:
        text, username = query.split("|")
    if replied and not query:
        await cat.reply("`Give username when replying to a message :(`")
        return
    if not replied and not query:
        await cat.reply("`Give me some text :(. Use .tweet message | username`")
        return
    try:
        a = await cat.reply(f"`Requesting {username} to tweet...`")
        text = deEmojify(text)
        catfile = await tweets(text, username)
        await cat.client.send_file(
            cat.chat_id, file=catfile, reply_to=cat.reply_to_msg_id
        )
        await cat.delete()
        await a.delete()
    except Exception as e:
        await cat.reply(str(e))


async def tweets(text1, text2):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text1}&username={text2}"
    ).json()
    pepe = r.get("message")
    if not pepe:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(pepe).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.webp", "webp")
    return "temp.webp"


@borg.on(admin_cmd(pattern="carry ?(.*)"))
async def trumptweet(event):
    args = event.pattern_match.group(1)
    if not args and not event.reply_to_msg_id:
        await event.reply("`Give some text to Carry Bish` 😒")
        await sleep(5)
        await event.delete()
        return
    if not args:
        replied = await event.get_reply_message()
        args = replied.text
    args = deEmojify(args)
    k = f"https://nekobot.xyz/api/imagegen?type=tweet&text={args}&username=CarryMinati"
    r = requests.get(k).json()
    meow = r.get("message")
    if not meow:
        return await event.edit("`Carryminati not found. He iz Busy :)`")
    a = await event.reply("`Carry Minati is Tweeting for You` 😎")
    await event.client.send_file(
        event.chat_id, file=meow, reply_to=event.reply_to_msg_id
    )
    await sleep(2)
    await event.delete()
    await a.delete()
