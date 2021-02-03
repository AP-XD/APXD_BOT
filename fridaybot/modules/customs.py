from fridaybot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"hhii ?(.*)"))  # initially made by @NOOB_GUY_OP
async def hhi(event):
    giveConfig = event.text
    a = giveConfig[5:6]
    if not a:
        a = "🌺"
    b = giveConfig[7:8]
    if not b:
        b = "✨"
    await event.edit(
        f"{a}{b}{b}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{a}{a}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{b}{a}{b}\n{a}{b}{b}{a}{b}{a}{a}{a}\n☁☁☁☁☁☁☁☁"
    )


# later made by me
@borg.on(admin_cmd(pattern=r"gws?(.*)"))
async def gws(event):
    giveConfig = event.text
    """m = giveConfig[5:-1]
    if not m:"""
    m = " Get Well Soon ! "
    a = giveConfig[-1:]
    if a == "s":
        a = "🌹"
    elif not a:
        a = "🌹"
    await event.edit(f"{a}{a}{a}{a}{a}{a}{a} \n{a} {m} {a}\n{a}{a}{a}{a}{a}{a}{a}")


@borg.on(admin_cmd(pattern=r"hii ?(.*)"))
async def hii(event):
    giveConfig = event.text
    a = giveConfig[5:6]
    if not a:
        a = "🌺"
    b = giveConfig[7:8]
    if not b:
        b = "✨"
    await event.edit(
        f"{b}{a}{b}{b}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{b}{b}\n{b}{a}{a}{a}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}"
    )


@borg.on(admin_cmd(pattern=r"hlo ?(.*)"))
async def hlo(event):
    giveConfig = event.text
    a = giveConfig[5:6]
    if not a:
        a = "🌺"
    b = giveConfig[7:8]
    if not b:
        b = "✨"
    await event.edit(
        f"{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{a}{a}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{a}{a}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{b}{b}{b}{b}{a}{b}{b}{a}{b}\n{b}{a}{b}{b}{a}{b}{a}{a}{a}{a}{b}{a}{a}{a}{a}{b}"
    )


@borg.on(admin_cmd(pattern=r"bye ?(.*)"))
async def bye(event):
    giveConfig = event.text
    a = giveConfig[5:6]
    if not a:
        a = "🌺"
    b = giveConfig[7:8]
    if not b:
        b = "✨"
    await event.edit(
        f"{a}{b}{b}{a}{a}{b}{a}{a}{a}{b}{a}{b}{b}{b}{a}\n{a}{b}{a}{b}{a}{a}{b}{a}{b}{a}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{a}{a}{a}{b}{a}{a}{a}{b}{b}{a}{a}\n{a}{b}{a}{b}{a}{a}{a}{b}{a}{a}{a}{b}{a}{a}{a}\n{a}{b}{b}{a}{a}{a}{a}{b}{a}{a}{a}{b}{b}{b}{a}"
    )
