from telethon import events
@bot.on(events.NewMessage(pattern=".prefix", incoming=True))
@bot.on(events.NewMessage(pattern=".prefix", outgoing=True))
@plus.on(events.NewMessage(pattern=".prefix", outgoing=True))
async def prefix(event):
	await event.reply(Var.COMMAND_HAND_LER + " 👈 is your current prefix for plugins")
	await event.delete()
