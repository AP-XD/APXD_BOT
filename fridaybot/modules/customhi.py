from fridaybot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"hhi ?(.*)"))
async def hhi(event):
    giveConfig = event.text
    cat = giveConfig[5:6]
    if not cat:
        cat = "🌺"
    ct = giveConfig[7:8]
    if not ct:
        ct = "✨"
    await event.edit(
        f"{cat}{ct}{ct}{cat}{ct}{cat}{cat}{cat}\n{cat}{ct}{ct}{cat}{ct}{ct}{cat}{ct}\n{cat}{cat}{cat}{cat}{ct}{ct}{cat}{ct}\n{cat}{ct}{ct}{cat}{ct}{ct}{cat}{ct}\n{cat}{ct}{ct}{cat}{ct}{cat}{cat}{cat}\n☁☁☁☁☁☁☁☁"
    )
