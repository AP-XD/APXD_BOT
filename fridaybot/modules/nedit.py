from fridaybot.utils import admin_cmd


@borg.on(admin_cmd(pattern="nchange (.*)"))
async def dead(nchange):
    name = nchange.pattern_match.group(1)
    A = f"✦҈͜͡➳🇮🇳{name}🇮🇳✦҈͜͡➳"
    await nchange.edit(A)
